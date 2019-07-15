FROM hub.ix.ai/docker/alpine:latest
LABEL ai.ix.maintainer="docker@ix.ai"
ARG PORT=9308

RUN pip3 install --no-cache-dir requests

ENV LOGLEVEL=INFO URL=https://data.ripple.com PORT=${PORT}

COPY src/ripple-exporter.py /

EXPOSE ${PORT}

ENTRYPOINT ["python3", "/ripple-exporter.py"]
