#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI

import requests
from utils.excel_data  import *
from utils.operationExcel import *
from utils.operationJson import *
from utils.operationExcel import *
class Method:
    def __init__(self):
        self.excel = OperationData()
        self.operationjson = OperationJson()
    def post(self,row):
        try:

            r=requests.post(
                url=self.excel.get_url(row=row),
                data = self.operationjson.get_json_data(row=row),
                headers=getRequestHeader(),
                timeout=6)
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
        return r
    def post(self,row,data):
        try:

            r=requests.post(
                url=self.excel.get_url(row=row),
                data = data,
                headers=getRequestHeader(),
                timeout=6)
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
        return r

class IsAssert:
    def __init__(self):
        self.excel=OperationData()
    def isContent(self,row,str2):
        flag=None
        if self.excel.get_Except(row=row) in str2:
            flag=True
        else:
            flag=False
        return flag