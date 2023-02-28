#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='ooop-wst',
    version='0.1.0',
    license='BSD',
    description='OOOP extension for using web services transactions with ws_transactions module',
    long_description='',
    url='http://github.com/gisce/ooop_wst',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    install_requires=['gisce-ooop', 'six'],
    py_modules=['ooop_wst'],
    platforms='any',
    keywords="openerp xml-rpc xmlrpc",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
