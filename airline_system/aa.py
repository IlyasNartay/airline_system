import os
import django

# Указываем, где находится файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_system.settings')

# Инициализируем Django
django.setup()

from django.contrib.auth.models import User

# Получаем всех пользователей, которые являются администраторами
admin_users = User.objects.filter(is_superuser=False)

# Выводим список админов
for admin in admin_users:
    print(admin.email)
