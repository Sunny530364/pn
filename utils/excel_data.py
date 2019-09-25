#!/usr/bin/python
# -*- coding: UTF-8 -*-

#author:ZHOGNQI

class ExcelVariable:
    CaseID=0
    url=2
    request_data=3
    Except=4
    Result=5
def getCaseID():
    return ExcelVariable.CaseID
def getUrl():
    return ExcelVariable.url
def getrequest_data():
    return ExcelVariable.request_data
def getExcept():
    return ExcelVariable.Except
def getResult():
    return ExcelVariable.Result
def getRequestHeader():
    '''获取请求头'''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie': '_ga=GA1.2.1237290736.1534169036; user_trace_token=20180813220356-b7e42516-9f01-11e8-bb78-525400f775ce; LGUID=20180813220356-b7e428ad-9f01-11e8-bb78-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFB3FA180CE47D5CD2C77E64B1B975127F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539433248,1539529521,1539785285,1540794503; _gid=GA1.2.675811712.1540794503; _gat=1; LGSID=20181029142824-d6b66331-db43-11e8-83f6-5254005c3644; PRE_UTM=; PRE_HOST=www.bing.com; PRE_SITE=https%3A%2F%2Fwww.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; SEARCH_ID=5e964af2d19e41f1903c1f4f5b41e1a5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540794522; LGRID=20181029142843-e1d2a63c-db43-11e8-83f6-5254005c3644',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'
    }
    return headers

