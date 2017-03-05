#!usr/bin/python3
from setuptools import setup

setup(name='virtberry_module_management',
	version='0.0.1',
	description='module management for virtberry',
	url='https://github.com/jonaschl/virtberry_module_management',
	author='Jonatan Schlag',
	author_email='jonatan@familyschlag.de',
	license='AGPLv3',
	include_package_data = True,
	packages=['virtberry_module_management'],
	zip_safe=False)
