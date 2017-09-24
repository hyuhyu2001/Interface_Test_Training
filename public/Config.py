#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

def url():
    url = 'http://httpbin.org/'
    # url = 'https://www.baidu.com/'
    return url

def mock_open():
    # open = 'ON'
    open = 'OFF'
    return open

#数据库连接串
sql_conn_dict = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'passwd':'123456',
    'db':'test',
    'charset':'utf8'
}

