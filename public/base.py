#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

from public import Config
from public import HttpService
from public import read_excel

def get_url(EndPoint):
    host = Config.url()
    endpoint = EndPoint
    url = ''.join([host, endpoint])
    return url

def get_response(url,Method,**DataALL):
    if Method == 'get':
        resp = HttpService.MyHTTP().get(url,**DataALL)
    elif Method == 'post':
        resp = HttpService.MyHTTP().post(url,**DataALL)
    return resp

def get_data(testfile,sheetname):
    datainfo = read_excel.XLDatainof(r'D:\python_pycharmWorkspace\python36\Interface_Test_Training\test_data\%s'%testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data