FROM python:3.11

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/backend

RUN chmod +x start.sh

