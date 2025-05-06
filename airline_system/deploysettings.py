from .settings import *
import os

DEBUG = False

hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

DEFAULT_ALLOWED = [
    "airline-system-pbjy.onrender.com",
    "localhost",
    "127.0.0.1"
]

if hostname:
    ALLOWED_HOSTS = [hostname] + DEFAULT_ALLOWED
    CSRF_TRUSTED_ORIGINS = ['https://' + hostname]
else:
    ALLOWED_HOSTS = DEFAULT_ALLOWED
    CSRF_TRUSTED_ORIGINS = ['https://' + host for host in DEFAULT_ALLOWED if not host.startswith("127.")]

