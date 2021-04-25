import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fh:
    long_description = fh.read()

setup(
    name='json2csv',
    version='0.0.1',
    author='Peter Begle',
    author_email='peterbegle@gmail.com',
    descrption='JSON to CSV CLI tool.',
    long_description=long_description,
    license='MIT',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        json2csv=json2csv:main
    ''',
    setup_requires=['pylint'],
    tests_require=['pytest', 'pytest-cov']
)
