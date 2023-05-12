run:
	python manage.py runserver

migrations:
	python manage.py makemigrations && python manage.py migrate

admin:
	python manage.py createsuperuser

checklist:
	python manage.py check --deploy

static files:
	python manage.py collectstatic

datadump:
	python manage.py dumpdata > data.json

test:
	python manage.py test

active:
	pipenv shell

inactive:
	deactivate


