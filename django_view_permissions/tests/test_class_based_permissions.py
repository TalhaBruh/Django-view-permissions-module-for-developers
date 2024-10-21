"""
Tests the functionality of Class based permissions.
"""
from unittest.mock import PropertyMock, patch

from ddt import data, ddt, unpack

from django_view_permissions.tests import BaseTestClass
from django_view_permissions.tests.test_app.permissions import AllowAccess, RejectAccess


@ddt
class ClassBasedPermissionsTests(BaseTestClass):
    """
    Tests the functionality of Class Based Permissions.
    """
    @unpack
    @data(
        # ........................................................
        (
            [('class', AllowAccess)],
            'GET',
            200
        ),
        (
            [('class', RejectAccess)],
            'GET',
            404
        ),
        (
            [('class', AllowAccess)],
            'POST',
            200
        ),
        (
            [('class', RejectAccess)],
            'POST',
            404
        ),
        # ........................................................
        (
            [('class', AllowAccess, ('GET'))],
            'GET',
            200
        ),
        (
            [('class', RejectAccess, ('GET'))],
            'GET',
            404
        ),
        (
            [('class', AllowAccess, ('GET'))],
            'POST',
            404
        ),
        (
            [('class', RejectAccess, ('GET'))],
            'POST',
            404
        ),
        # ........................................................
        (
            [('class', AllowAccess, ())],
            'GET',
            404
        ),
        (
            [('class', AllowAccess, ('GET', 'POST'))],
            'GET',
            200
        ),
        (
            [('class', RejectAccess, ('GET', 'POST'))],
            'POST',
            404
        ),
    )
    def test_class_based_permissions(self, permissions, request_method, return_value):
        """
        Tests the class based permissions functionality.
        """

        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=permissions
            ):
            self.call_view_and_assert_response('test-view', request_method, return_value)
