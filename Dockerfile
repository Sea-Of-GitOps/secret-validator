FROM python:3.12-slim

RUN useradd --create-home appuser

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "main.py"]
