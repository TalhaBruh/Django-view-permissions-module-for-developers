"""
Test urls for test app.
"""
from django.conf.urls import url

from django_view_permissions.tests.test_app import empty_view
from django_view_permissions.tests.test_app.views import test_view


# pylint: disable=invalid-name
urlpatterns = [
    url(r'^test', test_view, name='test-view'),
    url(r'^empty_view', empty_view, name='empty-view'),
]
