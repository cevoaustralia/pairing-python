from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open(path.join(here, 'utcservice/_version.py')) as f:
    exec(f.read(), version)

setup(
    name='utcservice',
    version=version['__version__'],
    description='Turn arbitrary date strings into UTC',
    long_description=long_description,
    author='Cevo',
    author_email='recruiting@cevo.com.au',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='recruitment training',
    packages=find_packages(exclude=['contrib','docs','tests']),
    install_requires=['flask','dateparser'],
    entry_points={
        'console_scripts': [
            'utcservice=utcservice:main',
        ]
    },
)
