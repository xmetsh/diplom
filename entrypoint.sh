#!/bin/bash
set -e

echo "📁 Текущая директория: $(pwd)"
echo "⚙️  Выполняем миграции..."

python manage.py makemigrations
python manage.py migrate

echo "🚀 Запускаем сервер..."
exec python manage.py runserver 0.0.0.0:8000
