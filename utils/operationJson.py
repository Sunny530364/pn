#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI
from utils.public import *
import json
from  utils.operationExcel import OperationData
class OperationJson:
    def __init__(self):
        self.excel=OperationData()

    def getReadJson(self):
        with open(data_dir(data='data',fileName='requestData.json'),encoding='utf-8') as f:
            data=json.load(f)
            return data
    def get_json_data(self,row):
        '''返回请求参数的值'''
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])

# opera=OperationJson()
# print(opera.get_json_data(1),type(opera.get_json_data(1)))




