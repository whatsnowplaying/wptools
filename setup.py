#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst', encoding='utf8') as f:
    readme = f.read()
with open('HISTORY.rst', encoding='utf8') as f:
    history = f.read()


setup(
    name='wptools',
    version='0.4.17',
    description='Wikipedia tools (for Humans)',
    long_description=readme + '\n\n' + history,
    url='https://github.com/siznax/wptools/',
    license='MIT',
    author='Steve @siznax',
    author_email='steve@siznax.net',
    py_modules=['wptools'],
    packages=find_packages(exclude=['tests']),
    test_suite='tests.test_basic',
    install_requires=['certifi', 'BeautifulSoup4', 'lxml'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['wptool=wptools.wptool:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
