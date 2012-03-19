#!/usr/bin/env python

from setuptools import setup

setup(
    name='BookType',
    version='1.0',
    description='OpenShift App',
    author='Your Name',
    author_email='areplogl@redhat.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django>=1.3','redis','simplejson','south','pil','lxml','unidecode','psycopg2']
)
#
