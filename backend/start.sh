#!/bin/sh

echo "🔄 Running migrations..."
python manage.py migrate

echo "👑 Creating superuser (if not exists)..."
python manage.py createsuperuser --noinput || true

echo "🖼️ Running collectstatics..."
python manage.py collectstatic --noinput

echo "🚀 Starting Django server..."
gunicorn store.wsgi