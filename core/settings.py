from pathlib import Path
import os, dj_database_url
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY','dev')
DEBUG = os.environ.get('DEBUG','true').lower()=='true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','localhost,127.0.0.1').split(',')

INSTALLED_APPS = ['django.contrib.contenttypes','django.contrib.auth','django.contrib.sessions','rest_framework','corsheaders','apps.health']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware']
ROOT_URLCONF='core.urls'
WSGI_APPLICATION='core.wsgi.application'

DATABASE_URL=os.environ.get('DATABASE_URL','sqlite:///'+str(BASE_DIR/'db.sqlite3'))
DATABASES={'default': dj_database_url.parse(DATABASE_URL)}

LANGUAGE_CODE='en-us'; TIME_ZONE='UTC'; USE_TZ=True
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
