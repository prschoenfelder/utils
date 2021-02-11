from setuptools import setup, find_packages

setup(
    name='prschoenfelder-utils',
    packages=find_packages(),
    url='https://github.com/prschoenfelder/utils',
    description='This contains a collection of util functions.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests==3.5.0"
        ],
    include_package_data=True,
) 
