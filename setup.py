#!/usr/bin/env python

from distutils.core import setup
import os

version = '0.01'

data = dict(
    name = 'upsWatcher',
    version = version,
    description = 'upsWatcher - A script to monitor a UPS and report status to Zabbix',
    author = 'David Whyte',
    author_email = 'david.whyte [at] gmail.com',

    script_data = ['upsWatcher'],
    data_files = [('/etc/init', ['upsWatcher.conf'])],
    )


setup(**data)
