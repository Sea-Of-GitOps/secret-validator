FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . ./

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER 1000:1000

ENTRYPOINT ["python"]
CMD ["main.py"]
