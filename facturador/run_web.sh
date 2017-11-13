#!/bin/sh
python manage.py migrate --settings=facturador.settings.prod
python manage.py collectstatic --no-input --settings=facturador.settings.prod
/usr/local/bin/gunicorn facturador.wsgi:application -w 2 -b :8000
