# Requirements
1. Python 3
2. Postgres

# Install
```
git clone https://github.com/waylostreamers/metadata_experiment.git
cd metadata_experiment

**On Sean's windows 10 running python 3.6 and 3.8**
python -m virtualenv venv && \
  source venv/Scripts/activate && \
  pip3 install -r requirements.txt && \
  deactivate  
  

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


#for sean
export DATABASE_URL=postgres://postgres@localhost:5432/waylo

python manage.py migrate
