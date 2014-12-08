import os
from setuptools import setup
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='base_theme',
    version='1.0',
    packages=['base_theme'],
    include_package_data=True,
    license='BSD License',
    description="A responsive base theme for Wharton Django applications.",
    url='https://github.com/chadwhitman/Base-Theme/',
    author='Chad Whitman, the Wharton School',
    data_files = [(' ', ['base_theme/templates/base.html']),],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
