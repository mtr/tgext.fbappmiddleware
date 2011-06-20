from setuptools import setup, find_packages
import os

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(name='tgext.fbappmiddleware',
      version=version,
      description="A TurboGears 2 middleware extension that provides a @expose_fb decorator to conditionally render Facebook application pages.",
      long_description=README,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: TurboGears"
        ],
      keywords='turbogears2.extension pylons',
      author='Martin Thorsen Ranang',
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
