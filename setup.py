import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

realpath = os.path.dirname(os.path.realpath('__file__'))
TEMPLATE_DIRS = os.path.join(realpath, "templates")
dataFiles = [(os.path.join(os.path.dirname(os.path.realpath('__file__')), "templates"), ['base_theme/templates/base.html']),]

setup(
    name='base_theme',
    version='1.0',
    packages=['base_theme'],
    package_data={'base_theme': [
        'templates/*.html',
        'templates/your_app/*.html',
        'templates/layout_options/*.html',
        'static/bootstrap_css/*.css',
        'static/fonts/*.*',
        'static/fonts/bask/*.*',
        'static/fonts/lato/*.*',
        'static/fonts/lus/*.*',
        'static/fonts/mont/*.*',
        'static/img/bg/*.*',
        'static/img/footer/*.png',
        'static/img/logo/*.png',
        'static/img/social/*.png',
        'static/js/*.js',
        'static/js/vendor/*.js',
        'static/scss/compiled_css/*.css',
        'static/scss/scss/*.scss',
        'static/scss/scss/base/*.scss',
        'static/scss/scss/components/*.scss',
        'static/scss/scss/helpers/*.scss',
        'static/scss/scss/layout/*.scss',
        'static/scss/scss/layout/header/*.scss',
        'static/*.*',
        'static/scss/config.rb',
    ]},
    include_package_data=True,
    data_files = [(os.path.join(os.path.dirname(os.path.realpath('__file__')), "templates"), ['base_theme/templates/base.html']),],
    license='BSD License',
    description="A responsive base theme for Wharton Django applications.",
    url='https://github.com/chadwhitman/Base-Theme/',
    author='Chad Whitman, the Wharton School',
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
