#!/bin/bash

docker exec catalog_db_1 \
  psql postgres://admin:password@localhost:5432/catalog \
  -c "CREATE SCHEMA content; GRANT ALL ON SCHEMA content TO admin;"

echo "Created content schema and granted access to admin postgres user"

docker exec catalog_django_1 \
  python manage.py migrate
echo "Migrated database"

docker exec catalog_django_1 \
  python manage.py createsuperuser --no-input
echo "Django superuser created"

echo "Django is ready to use."
