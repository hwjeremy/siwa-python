"""
Signin With Apple Python
PyPI Setup Module
author: hugh@blinkybeach.com
"""
from setuptools import setup, find_packages
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

with open(path.join(here, 'version'), encoding='utf-8') as version_file:
    VERSION = version_file.read()

setup(
    name='siwa',
    version=VERSION,
    description='Sign in with Apple',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/procuret/procuret-python',
    author='Hugh Jeremy',
    author_email='hugh@blinkybeach.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'

    ],
    keywords='library apple siwa signin',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    install_requires=[
        'PyJWT>=2.2.0',
        'rsa',
        'cryptography'
    ],
    project_urls={
        'Github Repository': 'https://github.com/hwjeremy/siwa-python',
        'About': 'https://github.com/hwjeremy/siwa-python'
    }
)
