from .settings import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    "airline-system-pbjy.onrender.com",
    "localhost",
    "127.0.0.1"
]

CSRF_TRUSTED_ORIGINS = [
    "https://airline-system-pbjy.onrender.com"
]