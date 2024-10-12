# Setting up Django, Nginx, and Gunicorn

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu

### Install Packages from Ubuntu Repos
```
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl -y
```

### Create the PostgreSQL Database and User
```
sudo -u postgres psql
```
Initialize the database and create an account
```
postgres=#: CREATE DATABASE myproject;
postgres=#: CREATE USER andreid WITH PASSWORD 'andreid';
```
Django expects `UTF-8` character encoding, and "read committed" blocks reads from uncommited transitions. Synchronize the Timezone and add the user admin
```
postgres=#: ALTER ROLE andreid SET client_encoding TO 'utf8';
postgres=#: ALTER ROLE andreid SET default_transaction_isolation TO 'read committed';
postgres=#: ALTER ROLE andreid SET timezone TO 'UTC';
postgres=#: GRANT ALL PRIVILEGES ON DATABASE myproject TO andreid;
```
Quit
```
postgres=#: \q
```
Postgres is now set up so that Django can connect to and manage its database information

### Set up the Virtual environment
Activate the virtual environment
```
source env/bin/activate
deactivate
```
pip install the following packages
```
pip install django gunicorn psycopg2-binary
```

### Create/configure new Django Project
Files that the Django project directory should have
- `~/level_django/manage.py`: A Django project management script.
- `~/level_django/myproject/`: The Django project package. This should contain the `__init__.py`, `settings.py`, `urls.py`, `asgi.py`, and `wsgi.py` files.
- `~/level_django/myprojectenv/`: The virtual environment directory you created earlier.
All of which can be achieved by:
```
django-admin startproject myproject .
```

Seting up `settings.py` with default fields (for Postgres and Nginx):
```
...
ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # Change this if needed
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
...
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

```

### Complete initial project setup

```
./manage.py makemigrations
./manage.py migrate
```
