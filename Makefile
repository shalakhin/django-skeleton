run:
	python manage.py runserver_plus

cs:
	python manage.py collectstatic --noinput

clear_cache:
	python manage.py clear_cache

test:
	ROOT_URLCONF="{{ project_name }}.urls" REUSE_DB=1 python manage.py test

migrate:
	python manage.py migrate

compass:
	cd static && compass watch

coffee:
	coffee -o static/js -wc static/coffee

specs:
	cd docs && xelatex -shell-escape *.tex
