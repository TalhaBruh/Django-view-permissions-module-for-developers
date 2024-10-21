import os

from setuptools import find_packages, setup

from django_view_permissions import VERSION


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.
    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included
        file
    """
    return not (
        line == '' or
        line.startswith('-r') or
        line.startswith('#') or
        line.startswith('-e') or
        line.startswith('git+') or
        line.startswith('-c')
    )


README = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')
).read()
CHANGELOG = open(
    os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')
).read()


setup(
    name='django-view-permissions',
    version=VERSION,
    author='ayub-khan',
    author_email='muhammadayubkhan6@gmail.com',
    url='https://github.com/Ayub-Khan/django-view-permissions',
    description='Utility to handle django view access',
    long_description=README + '\n\n' + CHANGELOG,
    long_description_content_type='text/x-rst',
    packages=find_packages(exclude=['tests']),
    license='Apache Software License 2.0',
    keywords='Django view permissions user',
    install_requires=load_requirements('requirements/base.in'),
    zip_safe=False,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
