from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)


def bad_request(request):
    """Custom 400 page"""
    response = render('400.html', {})
    response.status = 400
    return response


def forbidden(request):
    """Custom 403 page"""
    response = render('403.html', {})
    response.status = 403
    return response


def not_found(request):
    """Custom 404 page"""
    response = render('404.html', {})
    response.status = 404
    return response


def internal_error(request):
    """Custom 500 page"""
    response = render('500.html', {})
    response.status = 500
    return response


def csrf_error(request):
    """CSRF error"""
    response = render('csrf_error.html', {})
    response.status = 400
    return response
