#!/usr/bin/env python

from distutils.core import setup

setup(
    name='codebase',
    version='1.1',
    description='A Python client for the Codebase API',
    author='Phil Tysoe',
    author_email='philtysoe@gmail.com',
    url='https://github.com/igniteflow/codebase-python-api-client',
    packages=['codebase'],
    license='MIT',
    scripts=[
        'bin/codebase'
    ],
)
