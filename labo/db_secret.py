import os, sys
import dj_database_url

try:

    if "postgres://" in os.environ["DATABASE_URL"]:
        database_setting = {
            'default': {
                dj_database_url.config(default=os.environ["DATABASE_URL"])
            }
        }
    else:
        database_setting = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ["NSYS_DB_NAME"],
                'USER': os.environ["NSYS_DB_USER"],
                'PASSWORD': os.environ["NSYS_DB_PASS"],
                'HOST': os.environ["NSYS_DB_HOST"],
                'PORT': '5432',
            }
        }
except:
    database_setting = {}
