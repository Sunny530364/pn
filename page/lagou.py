#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI
from utils.operationExcel import *
from utils.operationJson import *
import json
operationJson=OperationJson()
def setso(kd='自动化测试工程师'):
    dict1=json.loads(operationJson.get_json_data(1))
    dict1['kd']=kd
    return dict1


