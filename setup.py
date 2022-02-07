#!/usr/bin/env python

from distutils.core import setup
from distutils.sysconfig import *

from setuptools import find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
install_reqs = parse_requirements('requirements.txt', session='hack')

try:
    reqs = [str(ir.req) for ir in install_reqs]
except:
    reqs = [str(ir.requirement) for ir in install_reqs]

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

cmdclass = {}
ext_modules = []

py_inc = [get_python_inc()]

setup(name='sample',
      version='0.2',
      description='data extractor',
      author='Synaptic',
      packages=find_packages(),
      install_requires=reqs,
      cmdclass=cmdclass,
      ext_modules=ext_modules
      )
