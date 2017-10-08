SETTINGS = "config.settings.dev"
PROJ = "config"

run:
	source .env/bin/activate; export DJANGO_SETTINGS_MODULE=$(SETTINGS); python manage.py runserver_plus 0.0.0.0:8000
	# source .env/bin/activate; export DJANGO_SETTINGS_MODULE=$(SETTINGS); python manage.py runserver

celery:
	source .env/bin/activate; export DJANGO_SETTINGS_MODULE=$(SETTINGS); celery -A config:celery_app worker -B -l info

test:
	source .env/bin/activate; export DJANGO_SETTINGS_MODULE=$(SETTINGS); REUSE_DB=1 python manage.py test

install:
	source .env/bin/activate; export DJANGO_SETTINGS_MODULE=$(SETTINGS);
	pip install -r requirements.txt

push:
	git push origin master

migrate:
	python manage.py migrate
	
clean_pyc:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete

makemessagesjs:
	python manage.py makemessages -d djangojs -a

makemessages:
	python manage.py makemessages -a

compilemessages:
	python manage.py compilemessages
