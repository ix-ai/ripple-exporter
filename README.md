# ripple-exporter

[![Pipeline Status](https://gitlab.com/ix.ai/ripple-exporter/badges/master/pipeline.svg)](https://gitlab.com/ix.ai/ripple-exporter/)
[![Docker Stars](https://img.shields.io/docker/stars/ixdotai/ripple-exporter.svg)](https://hub.docker.com/r/ixdotai/ripple-exporter/)
[![Docker Pulls](https://img.shields.io/docker/pulls/ixdotai/ripple-exporter.svg)](https://hub.docker.com/r/ixdotai/ripple-exporter/)
[![Gitlab Project](https://img.shields.io/badge/GitLab-Project-554488.svg)](https://gitlab.com/ix.ai/ripple-exporter/)

[Prometheus](https://prometheus.io) exporter for the [Ripple](https://ripple.com/) network, written in python

## Usage
```
docker run --rm -it -p 9999:9999 \
  -e LOGLEVEL=DEBUG \
  -e URL="https://data.ripple.com" \
  -e PORT=9999 \
  --name ripple-exporter \
  ixdotai/ripple-exporter:latest
```

## Supported variables
* `ADDRESSES` (no default) - comma separated list of the addresses monitor the balances
* `URL` (default: `https://data.ripple.com`) - the Ripple URL
* `GELF_HOST` (no default) - if set, the exporter will also log to this [GELF](https://docs.graylog.org/en/3.0/pages/gelf.html) capable host on UDP
* `GELF_PORT` (defaults to `12201`) - the port to use for GELF logging
* `PORT` (defaults to `9308`) - the listen port for the exporter
* `LOGLEVEL` (defaults to `INFO`)

## Resources:
* GitLab: https://gitlab.com/ix.ai/ripple-exporter
* Docker Hub: https://hub.docker.com/r/ixdotai/ripple-exporter

See also [ix.ai/crypto-exporter](https://gitlab.com/ix.ai/crypto-exporter) for more usage examples, including Prometheus configuration
