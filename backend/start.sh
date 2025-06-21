#!/bin/sh

echo "🔄 Running migrations..."
python manage.py migrate

echo "🖼️ Running collectstatics..."
python manage.py collectstatic --noinput

echo "🚀 Starting Django server..."
gunicorn store.wsgi