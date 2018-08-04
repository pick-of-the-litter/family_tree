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
    entry_points = {
        'console_scripts': [
            'family_tree = family_tree.__main__:main'
        ]
    },
    packages=['family_tree'],
    install_requires=[
        'pytest',
        'PEP8'
    ],
    include_package_data=True,
    zip_safe=False)