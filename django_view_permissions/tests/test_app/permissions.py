""" Test Permission Classes for test app. """


# pylint: disable=too-few-public-methods
class AllowAccess:
    """ Test class which allows all. """

    def __init__(self, request):
        """ test init method """

    def __call__(self):
        """ test call method """
        return True


# pylint: disable=too-few-public-methods
class RejectAccess:
    """ Test class which rejects all. """

    def __init__(self, request):
        """ test init method """

    def __call__(self):
        """ test call method """
        return False
