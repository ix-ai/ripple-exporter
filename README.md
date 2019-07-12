# ripple-exporter

[Prometheus](https://prometheus.io) exporter for the [Ripple](https://ripple.com/) network, written in python

## Usage
```
docker run --rm -it -p 9308:9308 \
  -e LOGLEVEL=DEBUG \
  -e API_KEY="your_api_key" \
  -e API_SECRET="your_api_secret" \
  -e FIAT="USD" \
  --name ripple-exporter \
  hub.ix.ai/docker/ripple-exporter:latest
```

## Supported variables
* `API_KEY` (no default) - set this to your Coinbase API key
* `API_SECRET` (no default) - set this to your Coinbase API secret
* `FIAT` (default: `EUR`) - the fiat currency for which to calculate the total transaction amount
* `LOGLEVEL` (defaults to `INFO`)
