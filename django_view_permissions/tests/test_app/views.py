""" Test App views Module """
from django_view_permissions.tests.test_app import BaseTestView


class TestView(BaseTestView):
    """
    Test View
    Initializing this with empty permissions
    so that each test case could add its own
    permissions.

    Example :

    permissions = [
        ('method', permissions.have_permission),
        ('attr', 'is_staff', True),
        ('class', permissions.BasicTestPermissions)
    ]

    """
    permissions = []


test_view = TestView.as_view()  # pylint: disable=invalid-name
