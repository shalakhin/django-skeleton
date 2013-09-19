from fabric.api import local


def deploy():
    """
    Deploy current build but test locally before push
    """
    local('make test')
    local('heroku maintenance:on --app {{ project_name }}')
    local('git push heroku master')
    local('heroku run --app {{ project_name }} make collectstatic')
    local('heroku run --app {{ project_name }} python manage.py syncdb --all')
    local('heroku run --app {{ project_name }} python manage.py clear_cache')
    local('heroku maintenance:off --app {{ project_name }}')

def install_heroku_postgres_addon():
    """
    Install Postgres heroku addon
    """
    local('heroku addons:add heroku-postgresql:dev')

def install_heroku_postgres_backups_addon():
    """
    Install Postgres backups heroku addon
    """
    local('heroku addons:add pgbackups:auto-month')
   
def install_heroku_redis_addon():
    """
    Install redis heroku addon
    """
    local('heroku addons:add redistogo:nano')

def install_heroku_sentry_addon():
    """
    Install sentry heroku addon
    """
    local('heroku addons:add sentry:developer')

def install_heroku_newrelic_addon():
    """
    Install new relic heroku addon
    """
    local('heroku addons:add newrelic:standard')

def install_heroku_cloudamqp_addon():
    """
    Install RabbitMQ heroku addon
    """
    local('heroku addons:add cloudamqp:lemur')

def install_heroku_addons():
    """
    Install all heroku addons at once
    """
    install_heroku_postgres_addon()
    install_heroku_postgres_backups_addon()
    install_heroku_redis_addon()
    install_heroku_sentry_addon()
    install_heroku_newrelic_addon()
    install_heroku_cloudamqp_addon()
