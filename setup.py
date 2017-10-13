#!/usr/bin/env python
from setuptools import setup

from tastu_teche import __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='tastu_teche',
      version=__version__,
      description='tastu_teche',
      long_description=readme(),
      author='Tastu Teche',
      author_email='tastuteche@yahoo.com',
      maintainer='Tastu Teche',
      maintainer_email='tastuteche@yahoo.com',
      url='https://github.com/tastuteche/tastu_teche',
      license="LGPL",
      keywords=['encoding', 'i18n', 'xml'],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   ("License :: OSI Approved :: GNU Library or Lesser General" +
                    " Public License (LGPL)"),
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ("Topic :: Software Development :: Libraries :: Python " +
                    "Modules"),
                   "Topic :: Text Processing :: Linguistic"],
      packages=['tastu_teche'],
      install_requires=[
          'redis', 'pycrypto', 'gntp'
      ],
      entry_points={'console_scripts': ['tastu_teche = tastu_teche.tastu_teche:main']})
