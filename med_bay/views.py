from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseForbidden


# Overriding the default 404 page
def error_404_handler(request, exception):
    return HttpResponseNotFound(render(request, 'errors/error_404.html'))


# Overriding the default 403 page
def error_403_handler(request, exception):
    return HttpResponseForbidden(render(request, 'errors/error_403.html'))
