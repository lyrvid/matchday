export DJANGO_SETTINGS_MODULE=matchday.settings

poetry install

poetry run ./manage.py migrate