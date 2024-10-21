"""
Middleware to handle access.
"""
from django.http import Http404
from django.urls import resolve

from django_view_permissions.access import CheckAcess


# pylint: disable=too-few-public-methods
class DjangoViewPermissionsMiddleware:
    """
    Main Middleware.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        view_func = resolve(request.path).func

        if hasattr(view_func, 'view_class') and \
                hasattr(view_func.view_class, 'permissions'):
            access = CheckAcess(request, view_func.view_class.permissions)
            if access.have_view_access():
                response = self.get_response(request)
                return response
            raise Http404
        response = self.get_response(request)
        return response
