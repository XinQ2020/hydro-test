"""
Author: Wenyu Ouyang
Date: 2022-06-28 21:29:43
LastEditTime: 2022-06-28 21:54:23
LastEditors: Wenyu Ouyang
Description: setup file
FilePath: \hydro-test\setup.py
Copyright (c) 2021-2022 Wenyu Ouyang. All rights reserved.
"""
#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "hydrotest", 
    version = "0.0.1", 
    keywords = ["test"], 
    description = "hydro test", 
    long_description = "a test repo for pypi packaging", 

    url = "https://github.com/OuyangWenyu/hydro-test",
    author = "Wenyu Ouyang", 
    author_email = "wenyuouyang@outlook.com",
    license= "MIT_license", 

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"], 
    python_requires='>=3.9', 
)
