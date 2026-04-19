
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt  --no-cache-dir

RUN useradd -m appuser && chown -R appuser:appuser /app

USER appuser
