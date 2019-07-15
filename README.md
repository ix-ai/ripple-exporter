# ripple-exporter

[Prometheus](https://prometheus.io) exporter for the [Ripple](https://ripple.com/) network, written in python

## Usage
```
docker run --rm -it -p 9999:9999 \
  -e LOGLEVEL=DEBUG \
  -e URL="https://data.ripple.com" \
  -e PORT=9999 \
  --name ripple-exporter \
  hub.ix.ai/docker/ripple-exporter:latest
```

## Supported variables
* `ADDRESSES` (no default) - comma separated list of the addresses monitor the balances
* `URL` (default: `https://data.ripple.com`) - the Ripple URL
* `GELF_HOST` (no default) - if set, the exporter will also log to this [GELF](https://docs.graylog.org/en/3.0/pages/gelf.html) capable host on UDP
* `GELF_PORT` (defaults to `12201`) - the port to use for GELF logging
* `PORT` (defaults to `9308`) - the listen port for the exporter
* `LOGLEVEL` (defaults to `INFO`)
