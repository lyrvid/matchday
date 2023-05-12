export DJANGO_SETTINGS_MODULE=matchday.settings

poetry install

django-admin makemigrations
django-admin migrate