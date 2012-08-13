# -*- coding: utf-8 -*-
from distutils.core import setup

classifiers = """\
Development Status :: 4 - Beta
Environment :: Console
License :: OSI Approved :: GNU General Public License (GPLv3)
Intended Audience :: Developers
Intended Audience :: End Users/Desktop
Operating System :: OS Independent
Programming Language :: Python
Topic :: Utilities
Topic :: Internet :: WWW/HTTP
Natural Language :: English
"""



setup(
    name='meteogp',
    version='0.1.2',
    author='Olivier Watte',
    author_email='olivier.watte@gmail.com',
    long_description=open('README.txt').read(),
    license='LICENSE.txt',
    plateforms='Any',
    install_requires=[
        "feedparser >= 5.0.0",    
    ],
    package_dir={'meteogp': ''},
    packages=['meteogp'],
    url='http://avaland.org',
    #classifiers=classifiers.split('\n'),
)


