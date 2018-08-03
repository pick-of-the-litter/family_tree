from setuptools import setup

def readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(name='Family Tree',
    version='0.1',
    author='Ash Murphy',
    author_email='amurphy9956@live.com',
    description='A simple console app to digitise a family tree',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['family_tree'],
    scripts=['bin/tree'],
    install_requires=[
        'pytest',
    ],
    include_package_data=True,
    zip_safe=False)