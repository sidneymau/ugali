import sys
import os
try: 
    from setuptools import setup, find_packages
except ImportError: 
    from distutils.core import setup
    def find_packages():
        return ['ugali','ugali.analysis','ugali.config','ugali.observation',
                'ugali.preprocess','ugali.simulation','ugali.candidate',
                'ugali.utils']

NAME = 'ugali'
HERE = os.path.abspath(os.path.dirname(__file__))
CLASSIFIERS = """\
Development Status :: 2 - Pre-Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
Programming Language :: Python
Natural Language :: English
Topic :: Scientific/Engineering
"""

from ugali.version import version as VERSION

def read(filename):
    return open(os.path.join(HERE,filename)).read()

setup(
    name=NAME,
    version=VERSION,
    url='https://bitbucket.org/bechtol/ugali/src',
    author='Keith Bechtol & Alex Drlica-Wagner',
    author_email='bechtol@kicp.uchicago.edu, kadrlica@fnal.gov',
    scripts = [],
    install_requires=[
        'python >= 2.7.0',
        'numpy >= 1.9.0',
        'scipy >= 0.14.0',
        'healpy >= 1.6.0',
        'pyfits >= 3.1',
        'emcee >= 2.1.0',
        'pyyaml >= 3.10',
    ],
    packages=find_packages(),
    package_data={'ugali': ['data/catalog.tgz']}
    description="Ultra-faint galaxy likelihood fitting code.",
    long_description=read('README.md'),
    platforms='any',
    classifiers = [_f for _f in CLASSIFIERS.split('\n') if _f]
)
