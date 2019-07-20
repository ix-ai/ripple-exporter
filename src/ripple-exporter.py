#!/usr/bin/env python3
"""Prometheus Exporter for the Ripple network """

import logging
import time
import os
import sys
import requests
import pygelf
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, GaugeMetricFamily

LOG = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get("LOGLEVEL", "INFO"),
    format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def configure_logging():
    """ Configures the logging """
    gelf_enabled: False

    if os.environ.get('GELF_HOST'):
        GELF = pygelf.GelfUdpHandler(
            host=os.environ.get('GELF_HOST'),
            port=int(os.environ.get('GELF_PORT', 12201)),
            debug=True,
            include_extra_fields=True,
            _ix_id=os.path.splitext(sys.modules['__main__'].__file__)[0],
        )
        LOG.addHandler(GELF)
        gelf_enabled = True
    LOG.info('Initialized logging with GELF enabled: {}'.format(gelf_enabled))


class RippleCollector:
    """ The RippleCollector class """
    accounts = {}
    settings = {}

    def __init__(self):
        self.settings = {
            'url': os.environ.get("URL", 'https://data.ripple.com'),
            'addresses': os.environ.get("ADDRESSES", '').split(','),
        }

    def get_ballance(self, address):
        """ Builds the connection and retrieves the balance for the given address """
        url = '{}/v2/accounts/{}/balances'.format(
            self.settings['url'],
            address
        )
        LOG.debug('URL: {}'.format(url))

        try:
            r = requests.get(url).json()
            LOG.debug('Response: {}'.format(r))
        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as error:
            LOG.exception('Exception caught: {}'.format(error))
        if r.get('result') == 'success' and r.get('balances'):
            for balance in r.get('balances'):
                LOG.debug('Registering balance {balance} for the currency {currency} - account {account}'.format(
                    balance=balance['value'],
                    currency=balance['currency'],
                    account=address
                ))
                self.accounts.update({
                    address: {
                        'value': float(balance['value']),
                        'currency': balance['currency'],
                        'type': 'ripple',
                    }
                })
        else:
            LOG.warning('Could not retrieve balance. The result follows.')
            LOG.warning('{}: {}'.format(r.get('result'), r.get('message')))

    def describe(self):
        """ Just a needed method, so that collect() isn't called at startup """
        return []

    def collect(self):
        """ The actual collector """
        metrics = {
            'account_balance': GaugeMetricFamily(
                'account_balance',
                'Account Balance',
                labels=['source_currency', 'currency', 'account', 'type']
            ),
        }
        for address in self.settings['addresses']:
            self.get_ballance(address=address)
        for account in self.accounts:
            metrics['account_balance'].add_metric(
                value=self.accounts[account]['value'],
                labels=[
                    self.accounts[account]['currency'],
                    self.accounts[account]['currency'],
                    account,
                    self.accounts[account]['type']
                ]
            )

        for metric in metrics.values():
            yield metric


if __name__ == '__main__':
    configure_logging()
    PORT = int(os.environ.get('PORT', 9308))
    LOG.info("Starting on port {}".format(PORT))
    REGISTRY.register(RippleCollector())
    start_http_server(PORT)
    while True:
        time.sleep(1)
