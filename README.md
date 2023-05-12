# Match Day API

A small, RESTful api for quotes

## Setup

1. Ensure you have python >=3.10 installed
2. Ensure you have [poetry](https://python-poetry.org/docs/) installed
3. Run the build script by executing `source build.sh` from the project root
4. Launch the webserver with the command `poetry run ./manage.py runserver`

## Development

### Using the admin panel
Django provides an admin panel that you can use to do various things, most notably 
edit the database (important as we are using sqlite3). Once you have run setup the 
project you can run the command `poetry run ./manage.py createsuperuser` and follow 
the prompts to set up the admin account username and password

### Changing the database models
The model classes in `models.py` control the schema of the underlying database. 
If you change them (update, add, remote, etc.) make sure to run 
`poetry run ./manage.py makemigrations matchday` to generate the required migrations 
to be applied to all dbs on startup.