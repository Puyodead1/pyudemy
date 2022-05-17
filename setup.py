from setuptools import setup

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='pyudemy',
    version='1.0.0',
    description='Python library for interacting with the Udemy API',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/Puyodead1/pyudemy',
    author='Puyodead1',
    author_email='puyodead@protonmail.com',
    license='GNU GPLv3',
    packages=['pyudemy'],
    install_requires=['requests'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)