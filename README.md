# Django Metadata Manager

The concept here is to manage content metadata using the Django framework, but not necessarily use this to directly back the user-facing app.

# Requirements
1. Python 3
2. Pipenv

# Install
```
pipenv install
pipenv shell
```

# Seed Database

To setup database with seed data:
```
pipenv shell
python manage.py migrate
python manage.py seed

# To explore data, you can use sqlite3
sqlite3 db.sqlite
```
