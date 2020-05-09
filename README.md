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
  
**On Sean's windows 10 running python 3.6 and 3.8**
python -m virtualenv venv && \
  source venv/bin/activate && \
  pip3 install -r requirements.txt && \
  deactivate  
  
 ** sean's path to "activate is venv/Scripts/activate
  

# POSTGRES is required
createdb waylo
psql postgres://localhost:5432/waylo
>>> CREATE SCHEMA content;
>>> GRANT ALL ON SCHEMA content TO admin;
>>> \q


** sean's postgres username is postgres not admin 
** GRANT ALL ON SCHEMA content TO postgres;


# Enter virtual environment
source venv/bin/activate



export DATABASE_URL=postgres://admin@localhost:5432/waylo

#for sean
export DATABASE_URL=postgres://postgres@localhost:5432/waylo

python manage.py migrate
```

# Seed Database (Currently not working)

To setup database with seed data:
```
python manage.py seed
```
