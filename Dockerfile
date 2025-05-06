# Dockerfile
FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Копируем проект
COPY . .

# Collect static (если у тебя есть STATICFILES)
RUN python manage.py collectstatic --noinput

# Открываем порт (необязательно, но можно)
EXPOSE 8000

# Команда запуска
CMD bash -c "python manage.py migrate && gunicorn airline_system.wsgi:application --bind 0.0.0.0:$PORT"
