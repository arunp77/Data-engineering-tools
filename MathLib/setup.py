# setup.py

from setuptools import setup, find_packages

setup(
    name='mathlib',
    version='0.1',
    packages=find_packages(),
    description='A simple math library with basic operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arun Kumar Pandey',
    author_email='arunp77@gmail.com',
    url='https://github.com/arunp77/Data-engineering-tools/matlib',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
