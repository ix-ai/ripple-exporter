FROM alpine:latest
LABEL maintainer="docker@ix.ai"

ARG PORT=9308
ARG LOGLEVEL=INFO
ARG URL=https://data.ripple.com

RUN apk --no-cache upgrade && \
    apk add --no-cache py3-requests && \
    pip3 install --no-cache-dir prometheus_client pygelf

ENV LOGLEVEL=${LOGLEVEL} URL=${URL} PORT=${PORT}

COPY src/ripple-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/ripple-exporter.py"]
