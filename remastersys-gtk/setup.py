#!/usr/bin/env python
# -*- coding:utf-8 -*-

import glob
from setuptools import setup, find_packages

setup(name = 'remastersys-gtk',
    version = '3.0.4',
    description='Ubuntu and variant system remaster. This is the alternate gtk gui for remastersys written in pygtk.',
    author='Tony Brijeski',
    author_email='tb6517@yahoo.com',
    url='http://www.remastersys.com',
    scripts=['remastersys-gtk'],
    packages = find_packages(),
    data_files = [
        ('share/remastersys-gtk/ui/', glob.glob('data/ui/*.glade')),
        ('share/remastersys-gtk/pixmaps/', glob.glob('data/pixmaps/*.png')),
        ('bin/', glob.glob('data/scripts/plymouth-preview')),
        ('share/man/man1/', glob.glob('man/man1/*.1')),
    ],
    license='GNU GPL',
    platforms='linux',
)
