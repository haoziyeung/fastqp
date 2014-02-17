from setuptools import setup, Extension
import distutils.core
import sys
import os

setup(
        name = 'fastqp',
        provides = 'fastqp',
        version = "0.1.0",
        author = 'Matthew Shirley',
        author_email = 'mdshw5@gmail.com',
        url = 'http://mattshirley.com',
        description = 'Simple NGS read quality assessment using Python',
        license = 'MIT',
        packages = ['fastqp'],
        entry_points = { 'console_scripts': [ 'fastqp = fastqp.cli:main' ] },
        classifiers = [
                "Development Status :: 3 - Alpha",
                "License :: OSI Approved :: MIT License",
                "Environment :: Console",
                "Intended Audience :: Science/Research",
                "Natural Language :: English",
                "Operating System :: Unix",
                "Programming Language :: Python :: 2.6",
                "Programming Language :: Python :: 2.7",
                "Programming Language :: Python :: 3.2",
                "Programming Language :: Python :: 3.3",
                "Topic :: Scientific/Engineering :: Bio-Informatics"
        ]
)
