#!/bin/bash

docker exec catalog_django_1 \
  python manage.py migrate
echo "Migrated database"

docker exec catalog_django_1 \
  python manage.py createsuperuser --no-input
echo "Django superuser created"

echo "Django is ready to use."
