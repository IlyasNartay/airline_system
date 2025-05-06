from .settings import *
import os

DEBUG = False

hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if hostname:
    ALLOWED_HOSTS = [hostname]
    CSRF_TRUSTED_ORIGINS = ['https://' + hostname]
else:
    ALLOWED_HOSTS = []
    CSRF_TRUSTED_ORIGINS = []
