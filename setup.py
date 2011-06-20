#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2011 by Martin Thorsen Ranang <mtr@ranang.org>

This file is part of tgext.FBAppMiddleware.

tgext.FBAppMiddleware is free software: you can redistribute it and/or
modify it under the terms of the Lesser GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

tgext.FBAppMiddleware is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Lesser
GNU General Public License for more details.

You should have received a copy of the Lesser GNU General Public
License along with tgext.FBAppMiddleware.  If not, see
<http://www.gnu.org/licenses/>.
"""
__author__ = "Martin Thorsen Ranang"
__version__ = '0.1'

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(name='tgext.fbappmiddleware',
      version=__version__,
      description="A TurboGears 2 middleware extension that provides a " \
      "@expose_fb_app decorator to conditionally render Facebook " \
      "application pages.",
      long_description=README,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: TurboGears"
        ],
      keywords='turbogears2.extension pylons',
      author=__author__,
      author_email='mtr@ranang.org',
      url='https://github.com/mtr/tgext.fbappmiddleware',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tgext'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
