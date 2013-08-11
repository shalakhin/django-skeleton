# -*- coding: utf-8 -*-
from fabric.api import local


def deploy():
    local('make test')
    local('heroku maintenance:on --app {{ project_name }}')
    local('git push heroku master')
    local('heroku run --app {{ project_name }} make cs')
    local('heroku run --app {{ project_name }} python manage.py syncdb --all')
    local('heroku run --app {{ project_name }} python manage.py clear_cache')
    local('heroku maintenance:off --app {{ project_name }}')

def install_heroku_postgres_addon():
    local('heroku addons:add heroku-postgresql:dev')

def install_heroku_postgres_backups_addon():
    local('heroku addons:add pgbackups:auto-month')
   
def install_heroku_redis_addon():
    local('heroku addons:add redistogo:nano')

def install_heroku_sentry_addon():
    local('heroku addons:add sentry:developer')

def install_heroku_newrelic_addon():
    local('heroku addons:add newrelic:standard')

def install_heroku_cloudamqp_addon():
    local('heroku addons:add cloudamqp:lemur')

def install_heroku_addons():
    """
    """
    install_heroku_postgres_addon()
    install_heroku_postgres_backups_addon()
    install_heroku_redis_addon()
    install_heroku_sentry_addon()
    install_heroku_newrelic_addon()
    install_heroku_cloudamqp_addon()
