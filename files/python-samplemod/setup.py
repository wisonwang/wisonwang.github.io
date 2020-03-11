# -*- coding: utf-8 -*-
# 注意养成好习惯 每个python文件头部定义 编码类型，否则在python文件解释过程中，会遇到中文编码问题
# Learn more: https://github.com/kennethreitz/setup.py
# 单行注释
"""
多行注释或者多行字符串，“"”和“'”可以通用
"""


from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# setup 函数式
setup(
    # 包名项目名， 当发布项目到pypi(https://pypi.org/)后，可以使用pip install <name>[==<version>], 安装项目
    name='sample',
    # 版本
    version='0.1.0',
    # 描述
    description='Sample package for Python-Guide.org',
    # 简要说明
    long_description=readme,
    # 作者信息
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    # 项目链接地址
    url='https://github.com/kennethreitz/samplemod',
    # 授权许可
    license=license,
    # find_packages，会搜索当前文件下的所有模块，作为项目模块（python模块是指包含"__init__.py"文件的目录），
    # 当执行pip install或者python setup.py install 命令时这些模块就会被安装到PYTHONPATH中
    # exclude 参数表示该程序包安装、打包时不包含目录
    packages=find_packages(exclude=('tests', 'docs'))
)
