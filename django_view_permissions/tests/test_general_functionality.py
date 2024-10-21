"""
Tests the functionality of middleware.
"""
from ddt import data, ddt

from django_view_permissions.tests import BaseTestClass


@ddt
class GeneralTests(BaseTestClass):
    """
    Genral Test cases of Permissions
    """
    @data('GET', 'POST')
    def test_empty_view(self, request_method):
        """
        Check empty view without permissions attribute works normaly.
        """
        self.call_view_and_assert_response('empty-view', request_method, 200)

    @data('GET', 'POST')
    def test_empty_permissions_reject_all_requests(self, request_method):
        """
        Tests if view permissions attr is empty all requests
        are rejected.
        """
        self.call_view_and_assert_response('test-view', request_method, 404)
