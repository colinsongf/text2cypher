#!/usr/bin/env
# -*- coding: utf-8 -*-
from setuptools import setup,find_packages



setup(
   name="text2cypher",
   version='1.0',
   packages = find_packages(exclude = ['docs', 'tests*']),
   author='domyoung',
   author_email='domyoung89@airi.kr',
   url='https://github.com/domyounglee/text2query',
   download_url  = 'https://github.com/domyounglee/text2query/dist/text2cypher-1.0-py3-none-any.whl',
   description="convert natural language query to graph db query ( cypher) using Universal Senetence Encoder ",
   include_package_data=True,
   install_requires=["numpy", "tensorflow","tensorflow_hub","pandas","spacy"],
   python_requires  = '>=3',
)