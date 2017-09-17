#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

def mockFoo(result):
    if result == 'success':
        mockData = {
            "request":{
                "method":"GET",
                "endpoint": "/api/testdetail",
                "params":{"show_env":1},
                "headers":{
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/58.0.3029.110 Safari/537.36",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive"
                }
            },
        "response":{
            "result": True,
            "status_code":400,
            "args": {"show_env": "1"},
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding":"gzip, deflate",
                "Connect-Time": "0",
                "Connection": "mock-close",
                "Host": "httpbin.org",
                "Total-Route-Time": "0",
                "User-Agent": "python-requests/2.13.0",
                "Via": "1.1 vegur",
                "X-Forwarded-For":"124.202.184.186",
                "X-Forwarded-Port": "80",
                "X-Forwarded-Proto": "http",
                "X-Request-Id": "a8813d21-0d66-4941-b124-5e92ece0b5bc",
                "X-Request-Start": "1505202044062"
            },
            "origin": "124.202.184.186",
            "url": "http://httpbin.org/get?show_env=1"
        }
    }
    else:
        mockData = {
            "request": {
                "method": "GET",
                "endpoint": "/api/testdetail"
                 },
            "response": {
                "result": False,
                "code":301,
                "msg":"请求方式不正确"
            }
        }
    return mockData.get('response')