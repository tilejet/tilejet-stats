#!/usr/bin/env python

from setuptools import setup

setup(
    name='tilejet-stats',
    version='0.0.1',
    install_requires=[],
    author='TileJet Developers',
    author_email='XXX',
    license='MIT License',
    url='https://github.com/tilejet/tilejet-stats/',
    keywords='python gis tilejet',
    description='A python utility library containing functions for generating statistics on tile service usage.',
    long_description=open('README.md').read(),
    download_url="https://github.com/tilejet/tilejet-stats/zipball/master",
    packages=["tilejetstats"],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
