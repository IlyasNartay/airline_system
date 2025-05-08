import os
import sys
import django
from pprint import pprint

# Добавь путь, если нужно
# sys.path.append('/path/to/project')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_system.settings')
django.setup()

from django.contrib.auth.models import User
from flights.serializers import UserSerializer

users = User.objects.filter(is_staff=True)
a = UserSerializer(users, many=True, context={'request': None}).data
pprint(a[0])
