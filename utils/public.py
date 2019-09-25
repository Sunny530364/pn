#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI

import os

def data_dir(data=None,fileName=None):
    '''查找文件的路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

