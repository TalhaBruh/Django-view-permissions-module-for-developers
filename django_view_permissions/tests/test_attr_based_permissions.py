"""
Tests the functionality of Attribute based permissions.
"""
from unittest.mock import PropertyMock, patch

from ddt import data, ddt, unpack

from django_view_permissions.tests import BaseTestClass


@ddt
class AttrBasedPermissionsTests(BaseTestClass):
    """
    Tests the functionality of Attribute Based Permissions.
    """
    @unpack
    @data(
        # ........................................................
        (
            [('attr', 'is_staff', True)],
            'GET',
            200
        ),
        (
            [('attr', 'is_staff', False)],
            'GET',
            404
        ),
        (
            [('attr', 'is_staff', True)],
            'POST',
            200
        ),
        (
            [('attr', 'is_staff', False)],
            'POST',
            404
        ),
        # ........................................................
        (
            [('attr', 'is_staff', True, ('GET'))],
            'GET',
            200
        ),
        (
            [('attr', 'is_staff', False, ('GET'))],
            'GET',
            404
        ),
        (
            [('attr', 'is_staff', True, ('GET'))],
            'POST',
            404
        ),
        (
            [('attr', 'is_staff', False, ('GET'))],
            'POST',
            404
        ),
        # ........................................................
        (
            [('attr', 'is_staff', True, ())],
            'GET',
            404
        ),
        (
            [('attr', 'is_staff', True, ('GET', 'POST'))],
            'GET',
            200
        ),
        (
            [('attr', 'is_staff', False, ('GET', 'POST'))],
            'POST',
            404
        ),
    )
    def test_attribute_based_permissions(self, permissions, request_method, return_value):
        """
        Tests the functionality of user attr based permissions.
        """
        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=permissions
            ):
            self.user.is_staff = True
            self.user.save()
            self.call_view_and_assert_response('test-view', request_method, return_value)
