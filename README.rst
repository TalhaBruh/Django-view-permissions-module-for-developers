django-view-permissions
=======================

|pypi-badge| |travis-badge| |docs-badge| |codecov-badge| |pyversions-badge|
|license-badge|

django-view-permissions provides ways to control access for Django app views

Overview
--------

Checks the incoming requests, to grant or deny access for views accoding to 
the permissions defined in the views. If permissions attribute is not defined
in the view, normal django flow is followed. If permissions attribute is
defined in view it checks and grants or denys access of the view.


Installation
------------

Install the latest release using pypi:

::

    pip3 install django-view-permissions

Add the application to the INSTALLED_APPS:

::

    INSTALLED_APPS = (
        ...
        # DjangoViewPermissions
        'django_view_permissions',
    )

Add the middleware to the configuration:

::

    MIDDLEWARE_CLASSES = (
        ...
        'django_view_permissions.middleware.DjangoViewPermissionsMiddleware',
    )

Usage
-----
Currently, 3 ways to define permissions are supported.

    - Attribute based permissions
    - Method based permissions
    - Class based permissions

Below is a Attribute based permission example. Where view will be only accessable
to users whose attribute 'is_staff' is 'True'. 

::

    class DummyView(View):
        permissions = [
            ('attr', 'is_staff', True),
        ]

In Method based permissions, you will need to defind the method with a 'request=None'
argument and a boolean return statement. All the requests for which method returns
'True' will be able to access the view.

::

    class DummyView(View):
        permissions = [
            ('method', permission_method),
        ]


In Class based permissions, you will need to defind a class with a 'request=None'
argument in __init__ method. All the requests for which __call__ method returns
'True' will be able to access the view.

::

    class DummyView(View):
        permissions = [
            ('class', PermissionClass),
        ]

Note: It is recommended to define the permission methods or classes in a separate file.

Please check `permissions.py <https://github.com/Ayub-Khan/django-view-permissions/blob/master/django_view_permissions/tests/test_app/permissions.py>`_ for examples.


License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/Ayub-Khan/django-view-permissions/blob/master/CONTRIBUTING.rst>`_ for details.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email muhammadayubkhan6@gmail.com.

Getting Help
------------

Feel free to create git issues in case of queries/issues/enhancements. 


.. |pypi-badge| image:: https://img.shields.io/pypi/v/django-view-permissions.svg
    :target: https://pypi.python.org/pypi/django-view-permissions/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.com/ayub-khan/django-view-permissions.svg?branch=master
    :target: https://travis-ci.com/ayub-khan/django-view-permissions
    :alt: Travis

.. |docs-badge| image:: https://readthedocs.org/projects/django-view-permissions/badge/?version=latest
    :target: https://django-view-permissions.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |codecov-badge| image:: http://codecov.io/github/ayub-khan/django-view-permissions/coverage.svg?branch=master
    :target: http://codecov.io/github/ayub-khan/django-view-permissions?branch=master
    :alt: Codecov

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/django-view-permissions.svg
    :target: https://pypi.python.org/pypi/django-view-permissions/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/ayub-khan/django-view-permissions.svg
    :target: https://github.com/Ayub-Khan/django-view-permissions/blob/master/LICENSE
    :alt: License
