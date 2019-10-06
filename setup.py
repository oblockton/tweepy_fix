#!/usr/bin/env python

# from distutils.core import setup
import re
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSIONFILE = "tweepymashup/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name="tweepymashup",
      version=version,
      description="Multi-Auth handling,Twitter library for python",
      long_description=long_description,
      license="MIT",
      author="O.G-Joshua Roesslein Remix-Nirg Mashup-oblockton",
      author_email="tweepy@googlegroups.com",
      url="https://github.com/oblockton/tweepy_fix",
      packages=find_packages(exclude=['tests', 'examples']),
      install_requires=[
          "PySocks>=1.5.7",
          "requests>=2.11.1",
          "requests_oauthlib>=0.7.0",
          "six>=1.10.0",
      ],
      keywords="twitter library",
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=True)
