"""
Test Module for django-view-permissions.
"""
from unittest.mock import PropertyMock, patch

from django.contrib.auth.models import User
from django.test.testcases import TestCase
from django.urls import reverse

from django_view_permissions.tests.test_app.permissions import AllowAccess, RejectAccess


class BaseTestClass(TestCase):
    """
    View Permission Middleware Tests
    """

    def setUp(self):
        super(BaseTestClass, self).setUp()
        self.user = User.objects.create_user(username='test')
        self.client.force_login(self.user)

    def call_view_and_assert_response(self, view, request_method, status_code):
        """
        Calls the View, checks the response.
        """
        if request_method == 'GET':
            response = self.client.get(reverse(view))
        else:
            response = self.client.post(reverse(view))

        self.assertEqual(response.status_code, status_code)
        if status_code == 200:
            self.assertEqual(response.content.decode('utf-8'), 'ok!')

    def tearDown(self):
        super(BaseTestClass, self).tearDown()
        self.client.logout()
        self.user.delete()
