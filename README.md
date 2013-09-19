# django-skeleton

## Why?

To save others and my time I decided to make great django-skeleton considering
**best practices** used by django developers all over the world. If you find
something you'd like to be added pull requests or issues are highly appreciated.

## What's in?

* fabric with deployment on heroku

```bash
fab install_heroku_addons
fab deploy
```

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

* bower to install necessary dependencies and don't look where is my jquery
  etc.

```
bower install
```

* divided requirements for development, production and testing
* divided settings for development, production and testing

## Usage

```bash
django-admin.py startproject --template=https://github.com/OShalakhin/django-skeleton/archive/master.zip new_project
```

To launch heroku web app with this skeleton:

```bash
django-admin.py startproject --template=https://github.com/OShalakhin/django-skeleton/archive/master.zip new_project

heroku create
heroku app:rename new_project
fab install_heroku_addons
git commit -m "my first commit"
fab deploy
```

## TODO

- [x] add `fabfile.py`
- [ ] add `thirdparties.sh` to install `coffeescript`, `compass`, `sass`, `backbone` etc.
- [ ] add `hooks` for validation of `print...`, `console.log...`, `import ipdb...`
- [x] review `requriements/`
- [x] review `settings/`
