# Django Metadata Manager

The concept here is to manage content metadata using the Django framework, but not necessarily use this to directly back the user-facing app.

# Requirements
1. Python 3
2. Postgres

# Install
```
git clone https://github.com/waylostreamers/metadata_experiment.git
cd metadata_experiment

# Install dependencies
python3 -m virtualenv venv && \
  source venv/bin/activate && \
  pip3 install -r requirements.txt && \
  deactivate

# POSTGRES is required
createdb waylo
psql postgres://localhost:5432/waylo
>>> CREATE SCHEMA content;
>>> GRANT ALL ON SCHEMA content TO admin;
>>> \q

# Enter virtual environment
source venv/bin/activate

export DATABASE_URL=postgres://admin@localhost:5432/waylo

python manage.py migrate
```

# Seed Database (Currently not working)

To setup database with seed data:
```
python manage.py seed
```
