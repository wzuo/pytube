#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains setup instructions for pytube."""
import codecs
import os
import sys
from shutil import rmtree

from setuptools import Command
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()


class UploadCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds ...')
            rmtree(os.path.join(here, 'dist'))
        except Exception:
            pass
        self.status('Building Source distribution ...')
        os.system('{0} setup.py sdist bdist_wheel'.format(sys.executable))
        self.status('Uploading the package to PyPI via Twine ...')
        os.system('twine upload dist/*')
        sys.exit()


try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]


setup(
    name='pytube',
    version='9.5.3',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    packages=['pytube', 'pytube.contrib'],
    package_data={
        '': ['LICENSE'],
    },
    url='https://github.com/nficano/pytube',
    install_requires=load_requirements("requirements.txt"),
    license='MIT',
    entry_points={
        'console_scripts': [
            'pytube = pytube.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    description=('A pythonic library for downloading YouTube Videos.'),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    zip_safe=True,
    cmdclass={'upload': UploadCommand},
)
