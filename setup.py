from setuptools import setup, find_packages
import sys

requirements = [
    'requests',
    'random',
]

if sys.platform != 'win32':
    requirements.append('some-unix-only-package')

setup(
    name='ezusergen',
    version='0.1.0',
    description='A simple username generator that combines random words with numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ondry',
    author_email='ondrygfx@gmail.com',
    url='https://github.com/Ondry4K/ezusergen',
    packages=find_packages(),
    install_requires=[
        'requests',
        'random',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
