#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='rivr_peewee',
    version='0.1.0',
    description='rivr integration for the peewee database ORM.',
    url='https://github.com/rivrproject/rivr-peewee',
    packages=find_packages(),
    install_requires=[
        'rivr',
        'peewee'
    ],
    author='Kyle Fuller',
    author_email='inbox@kylefuller.co.uk',
    license='BSD'
)

