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

### Loading sample data
You can load up some sample data by running the command 
`poetry run ./manage.py loaddata tests/unit/example_db.json` from the project root

### Running the tests
Tests can be run using the command `poetry run ./manage.py test`. Mock data is populated
via the json file `example_db.json`

## API

### `/qotd`

Pull a random quote from the database

#### Example response
```json
{
  "quote": "Cheese is tasty",
  "author": {
    "first_name": "Mr.",
    "last_name": "Mouse"
  }
}
```

#### Returns `404` if no quotes in the database

### `/authors`

Pull all the authors from the database

#### Example response
```json
{
  "authors": [
    {
        "first_name": "Mr.",
        "last_name": "Mouse"
    }
  ]
}
```

### `/quotd/Mr. Mouse`

Pull a random quote from the defined author from the database
First name and last name must be provided in the url

#### Example response
```json
{
  "quote": "Cheese is tasty",
  "author": {
    "first_name": "Mr.",
    "last_name": "Mouse"
  }
}
```

#### Will return `404` if no quote/author exists that matches

### `/quotd/zen`

Pull a random quote from the ZenQuotes API

#### Example response
```json
{
  "quote": "Cheese is tasty",
  "author": {
    "first_name": "Mr.",
    "last_name": "Mouse"
  }
}
```

#### Will return `500` if unable to get a quote from zenquotes's API

## Scope reduction
1. Make endpoints asynchronous, future proofs complicated work
2. Dynamically generate the OpenAPI specification for all the endpoints