"""
setup.py for Flask-Limiter-graphQL-support


"""
__author__ = "Julien Gaye"
__email__ = "julien@getluko.com"
__copyright__ = "Copyright 2019, Julien Gaye"

from setuptools import setup, find_packages
import os

this_dir = os.path.abspath(os.path.dirname(__file__))
REQUIREMENTS = filter(None, open(
    os.path.join(this_dir, 'requirements', 'main.txt')).read().splitlines())

import versioneer

setup(
    name='Flask-Limiter-graphQL-support',
    author=__author__,
    author_email=__email__,
    license="MIT",
    url="",
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=list(REQUIREMENTS),
    classifiers=[k for k in open('CLASSIFIERS').read().split('\n') if k],
    description='Rate limiting for flask applications, with graphQL queries and mutations rate limiting',
    long_description=open('README.rst').read() + open('HISTORY.rst').read(),
    packages=find_packages(exclude=["tests*"]),
)

