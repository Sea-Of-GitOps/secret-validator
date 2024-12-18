FROM python:3.12-alpine

WORKDIR /app

COPY . /app

RUN apk update && apk add --no-cache \
    libpq-dev gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev && \
    rm -rf /var/cache/apk/*

USER 1000:1000

ENTRYPOINT ["python"]
CMD ["main.py"]
