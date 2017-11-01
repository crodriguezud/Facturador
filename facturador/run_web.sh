#!/bin/sh
python manage.py migrate --settings=settings
python manage.py collectstatic --no-input --settings=settings
/usr/local/bin/gunicorn wsgi:application -w 2 -b :8000
