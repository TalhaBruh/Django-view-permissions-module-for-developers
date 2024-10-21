"""
Tests the functionality of Method based permissions.
"""
from unittest.mock import PropertyMock, patch

from ddt import data, ddt, unpack

from django_view_permissions.tests import BaseTestClass


@ddt
class MethodBasedPermissionsTests(BaseTestClass):
    """
    Tests the functionality of Method Based Permissions.
    """

    @unpack
    @data(
        # ........................................................
        (
            [('method', lambda request: True)],
            'GET',
            200
        ),
        (
            [('method', lambda request: False)],
            'GET',
            404
        ),
        (
            [('method', lambda request: True)],
            'POST',
            200
        ),
        (
            [('method', lambda request: False)],
            'POST',
            404
        ),
        # ........................................................
        (
            [('method', lambda request: True, ('GET'))],
            'GET',
            200
        ),
        (
            [('method', lambda request: False, ('GET'))],
            'GET',
            404
        ),
        (
            [('method', lambda request: True, ('GET'))],
            'POST',
            404
        ),
        (
            [('method', lambda request: False, ('GET'))],
            'POST',
            404
        ),
        # ........................................................
        (
            [('method', lambda request: True, ())],
            'GET',
            404
        ),
        (
            [('method', lambda request: True, ('GET', 'POST'))],
            'GET',
            200
        ),
        (
            [('method', lambda request: False, ('GET', 'POST'))],
            'POST',
            404
        ),
    )
    def test_method_based_permissions(self, permissions, request_method, return_value):
        """
        Tests the method based permissions functionality.
        """
        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=permissions
            ):
            self.call_view_and_assert_response('test-view', request_method, return_value)
