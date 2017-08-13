#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

from public import Config
from public import HttpService

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
