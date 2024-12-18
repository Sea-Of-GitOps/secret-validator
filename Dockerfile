FROM python:3.12-slim

WORKDIR /app

COPY . /app
RUN python -m ensurepip --upgrade && pip install -r requirements.txt


RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc && \
    apt-get autoremove -y gcc && \
    rm -rf /var/lib/apt/lists/*

USER 1000:1000

ENTRYPOINT ["python"]
CMD ["main.py"]
