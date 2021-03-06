# Django Metadata Manager

The concept here is to manage content metadata using the Django framework, but not necessarily use this to directly back the user-facing app.

# Setup the Easy Way - with docker for mac

## Requirements
1. Docker (https://docs.docker.com/docker-for-mac/install/)
2. Docker Compose (https://docs.docker.com/compose/install/)

After installing both of the above:
## Install
```
git clone https://github.com/waylostreamers/catalog.git
cd catalog

docker-compose up -d
./setup.sh
```
You should now be able to go to http://localhost:8000/admin
and login to the Django admin UI with the username "admin" and password "password".

To kill the docker containers (this will also destroy the database):
```
docker-compose down
```

To call django management commands, use the django helper script:
```
./django migrate
# is equivalent to:
python manage.py migrate
# except that it runs inside the docker container
```

# Seed DB and run demo app

To seed database with fake data:
After running `docker-compose up -d` & `./setup.sh`:
```
./django seed --users 10
```
to create 10 fake users along with randomized artists and tracks.

Then when you navigate to `localhost:8000` you should be able to view the fake data in the app.


# Setup - without docker
## Requirements
1. Python 3
2. Postgres

# Install
```
git clone https://github.com/waylostreamers/catalog.git
cd catalog

# Install dependencies
python3 -m virtualenv venv && \
  source venv/bin/activate && \
  pip3 install -r requirements.txt && \
  deactivate
  
  
# POSTGRES is required
createdb catalog
psql postgres://localhost:5432/catalog
>>> CREATE SCHEMA content;
>>> GRANT ALL ON SCHEMA content TO admin;
>>> \q


GRANT ALL ON SCHEMA content TO postgres;


# Enter virtual environment
source venv/bin/activate

export DATABASE_URL=postgres://admin@localhost:5432/catalog

python manage.py migrate
```

# Python Docs View

You can browse auto-generated documentation from the source code by doing the following:
1. Ensure you have an up-to-date virtualenv
```
source venv/bin/activate
pip install -r requirements
```
2. Add a django superuser
```
python manage.py createsuperuser
...
```
3. Run the django server
```
python manage.py runserver
```
4. Go to `localhost:8000/admin/doc/` in your browser



# To commit your code 

```
docker exec catalog_django_1 black content
git status
git add .
git commit -m "commit message " 
git push --set-upstream origin <branch_name>
``` 

