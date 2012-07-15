#!/usr/bin/env python
from distutils.core import setup
import setuptools

setup(name='ravelryshow',
      version='1.0',
      description='Pyramid app for showing ravelry data',
      author='Jacinda Moore',
      author_email='alynna.kasmira@gmail.com',
      url='https://github.com/lavaturtle/show-ravelry-data',
      packages=['ravelryshow'],
      requires=['pyramid'])
