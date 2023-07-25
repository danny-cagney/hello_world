import os
import re
import sys

# get the version from the module without importing it
from helloworld import __version__ as version

readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()

# This file is used to install the application
SETUP_ARGS = dict (
    name='hello_world',  # The name of the application
    version=version,  # This is the version of the application
    description=('This program is used as an example of how to structure the files for a Python application.\
               It grabs the "Hello World" title from Wikipedia and prints the title'),
    # Read the README.md file for the long description
    long_description=long_description,
    url='https://github.com/danny-cagney/hello_world',  # The URL for the application
    author='<Author Name>',
    author_email='<Author Email>',
    license='MIT',  # The license for the application
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ], py_modules=['helloworld',],  # The modules for the application
    # The dependencies for the application
    install_requires = [
        'requests>=2.22',
        ],
)


if __name__ == '__main__':
    from setuptools import setup, find_packages

    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)
