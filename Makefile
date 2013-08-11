run:
	python manage.py runserver_plus

collectstatic:
	python manage.py collectstatic --noinput

makemessages:
	python manage.py makemessages -a

compilemessages:
	python manage.py compilemessages

test:
	python manage.py test
	
clean_pyc:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete

makemessagesjs:
	python manage.py makemessages -d djangojs -a

migrate:
	python manage.py migrate
