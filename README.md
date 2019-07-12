# ripple-exporter

[Prometheus](https://prometheus.io) exporter for the [Ripple](https://ripple.com/) network, written in python

## Usage
```
docker run --rm -it -p 9308:9308 \
  -e LOGLEVEL=DEBUG \
  -e URL="https://data.ripple.com"
  --name ripple-exporter \
  hub.ix.ai/docker/ripple-exporter:latest
```

## Supported variables
* `ADDRESSES` (no default) - comma separated list of the addresses monitor the balances
* `URL` (default: `https://data.ripple.com`) - the Ripple URL
* `LOGLEVEL` (defaults to `INFO`)
