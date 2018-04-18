# coding:utf-8
from distutils.core import setup, Extension

module1 = Extension('VLTest',
                    sources = ['src/VLTestClib.c','src/VLTestCLibWrap.c'])

setup (name = 'VLTest',
       version = '1.0',
       description = u'变值特性测量C扩展',
       ext_modules = [module1])