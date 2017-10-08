# django-skeleton

## Why?

To save others and my time I decided to make great django-skeleton considering
**best practices** used by django developers all over the world. If you find
something you'd like to be added pull requests or issues are highly appreciated.

## What's in?

* Makefile to reduce console typing

```bash
make run
make collectstatic
make makemessages
make compilemessages
make test
make clean_pyc
make makemessagesjs
make migrate
```

## Usage

```bash
django-admin.py startproject --template=https://github.com/shalakhin/django-skeleton/archive/master.zip new_project
```

To launch heroku web app with this skeleton:

```bash
django-admin.py startproject --template=https://github.com/shalakhin/django-skeleton/archive/master.zip new_project

heroku create
heroku app:rename new_project
fab install_heroku_addons
git commit -m "my first commit"
```
