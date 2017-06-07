#!coding:utf8
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup
VERSION = "3.0.0"


if __name__ == "__main__":
    setup(
        name="geetest",
        version=VERSION,
        packages=['geetest'],
        url='https://github.com/zhouziqunzzq/geetest_py',
        license='',
        author='Geetest',
        author_email='admin@geetest.com',
        description='Geetest Python SDK',
        install_requires='requests>=2.6.0',
    	)
