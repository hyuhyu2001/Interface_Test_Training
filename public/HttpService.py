#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

import requests
import json
from public import Config

class MyHTTP(object):
    def __init__(self):
        self.url = Config.url()

    def get(self,url,**DataALL):
        # params = DataALL.get('params')
        # headers = DataALL.get('headers')
        try:
            resp = requests.get(url, **DataALL,timeout=3)
            # resp = requests.get(url,params=params,headers=headers,timeout=3)
            text = resp.json()
            return text
        except Exception as e:
            print('GET错误:%s' % e)

    def post(self,url,**DataALL):
        # params = DataALL.get('params')
        # headers = DataALL.get('headers')
        # data = DataALL.get('data')
        # json = DataALL.get('json')
        # files = DataALL.get('files')
        try:
            resp = requests.post(url, **DataALL, timeout=3)
            # resp = requests.post(url,params=params,headers=headers,data=data,json=json,files=files,timeout=3)
            text = resp.json()
            return text
        except Exception as e:
            print('POST错误:%s' % e)