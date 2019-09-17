FROM python:3.7-alpine

WORKDIR /opt/app-a
COPY . /opt/app-a

RUN apk add --no-cache --virtual .deps \
        gcc make musl-dev && \
    pip install responder httpx && \
    apk del --purge .deps

CMD ["python", "main.py"]
