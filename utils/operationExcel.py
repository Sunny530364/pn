#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI

import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *

class OperationData:
    def getExcel(self):
        db=xlrd.open_workbook(data_dir('data','data.xls'))
        sheet=db.sheet_by_index(0)
        return sheet
    def get_rows(self):
        '''获取excel的行数'''
        return self.getExcel().nrows
    def get_rows_cel(self,row,col):
        return self.getExcel().cell_value(row,col)
    def get_CaseID(self,row):
        '''获取测试ID'''
        return self.get_rows_cel(row,getCaseID())
    def get_url(self,row):
        '''获取请求地址'''
        return self.get_rows_cel(row,getUrl())
    def get_request_data(self,row):
        '''获取请求参数'''
        return self.get_rows_cel(row,getrequest_data())
    def get_Except(self,row):
        '''获取期望结果'''
        return self.get_rows_cel(row,getExcept())
    def get_result(self,row):
        '''获取实际结果'''
        return self.get_rows_cel(row,getResult())


operation=OperationData()
print(operation.get_Except(1))



