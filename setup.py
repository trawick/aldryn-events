# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages
from aldryn_events import __version__

py26 = sys.version_info < (2, 7, 0) and sys.version_info >= (2, 6, 0)
py27 = sys.version_info < (2, 8, 0) and sys.version_info >= (2, 7, 0)
py3k = sys.version_info >= (3, 3, 0)  # for u'unicode' syntax

if not py26 and not py27 and not py3k:
    raise ValueError(
        "Aldryn Events currently supports Python 2.6, 2.7, 3.3, and higher, "
        "not {0}".format(sys.version_info)
    )

REQUIREMENTS = [
    'aldryn-apphooks-config>=0.1.4',
    'aldryn-boilerplates',
    'aldryn-common>=0.0.6',
    'aldryn-translation-tools>=0.2.1',
    'aldryn-reversion>=1.0.0,<1.1.0',
    'django-appconf',
    'django-appdata<0.2',
    'django-bootstrap3',
    'django-cms>=3.0.12',
    'django-extended-choices',
    'django-filer',
    'django-parler',
    'django-sortedm2m',
    'django-standard-form>=1.1.1',
    'djangocms-text-ckeditor',
    'python-dateutil',
]

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
if py26:
    REQUIREMENTS += [
        'Django>=1.6,<1.7',
        'South>=1.0.2,<1.1',
    ]

if py27 or py3k:
    REQUIREMENTS += [
        'Django>=1.6,<1.9',
    ]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.6',
    'Framework :: Django :: 1.7',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='aldryn-events',
    version=__version__,
    description='An events app for Aldryn',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-events',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
)
