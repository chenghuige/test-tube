#!/usr/bin/env python
from setuptools import find_packages, setup

version = '0.611'

setup(
    name='test_tube',
    packages=find_packages(),
    version=version,
    description='Experiment logger and visualizer',
    author='William Falcon',
    install_requires=[
        'pandas>=0.20.3',
        'numpy>=1.13.3',
        'imageio>=2.3.0'
    ],
    author_email='will@hacstudios.com',
    url='https://github.com/williamFalcon/test_tube',
    download_url='https://github.com/williamFalcon/test_tube/archive/{}.tar.gz'.format(version),
    keywords=[
        'testing',
        'machine learning',
        'deep learning',
        'prototyping',
        'experimenting',
        'modeling',
    ],
)
