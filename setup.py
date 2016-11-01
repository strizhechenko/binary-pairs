#!/usr/bin/env python

'''Heil to combinatoric explosion reduce!'''

import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='binary-pairs',
    version='0.0.3',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    license='GPL',
    url='https://github.com/strizhechenko/binary-pairs',
    keywords='combinatoric testing utils fuzz pairwise nwise reduce',
    description='Utility designed for check combinations of multiple binary params',
    long_description=(read('README.rst')),
    packages=find_packages(exclude=['tests*']),
    scripts=['utils/binary-pairs'],
    install_requires=['AllPairs'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
