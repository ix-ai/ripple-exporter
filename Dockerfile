FROM hub.ix.ai/docker/alpine:latest
LABEL ai.ix.maintainer="docker@ix.ai"

ENV LOGLEVEL=INFO URL=https://data.ripple.com

COPY ripple-exporter.py /

EXPOSE 9308

ENTRYPOINT ["python3", "/coinbase-exporter.py"]
