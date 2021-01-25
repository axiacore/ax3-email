from setuptools import setup

__VERSION__ = '0.0.1'

with open('README.md', 'r') as fh:
	long_description = fh.read()

setup(
	name='AX3 EmailBackend',
	version=__VERSION__,
	description='A Django app to send emails using Huey tasks',
	long_description_content_type='text/markdown',
	long_description=long_description,
	url='https://github.com/Axiacore/ax3-email-backend',
	author='Axiacore, ',
	author_email='info@axiacore.com',
	include_package_data=True,
)
