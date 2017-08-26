#!/usr/bin/env python

"""
@author:     巧吧软件测试
@desc:无请求参数
"""

import requests
import json
import unittest
from public import base
from ddt import ddt,data,unpack

testcasefile = 'get_nothing_test_data.xlsx'
AllData = base.get_data(testcasefile, 'AllData')
TestData = base.get_data(testcasefile, 'TestData')[1:]

@ddt
class GetNothingTest(unittest.TestCase):
    '''GET无参数测试'''
    def setUp(self):
        self.endpoint = AllData[1][1]
        self.RequestMethod = AllData[1][2]
        self.RequestData = AllData[1][3]
        self.url = base.get_url(self.endpoint)

    @data(*TestData)
    @unpack
    def test_2(self,*TestData):
        '''校验headers里的Connection值'''
        Method = self.RequestMethod
        if self.RequestData != '':
            DataAll = eval(self.RequestData)
            resp = base.get_response(self.url,Method,**DataAll)
        else:
            resp = base.get_response(self.url, Method)

        connect = resp[TestData[0]][TestData[1]]
        self.assertEqual(connect,TestData[2])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
        # print(r.url)#获取URL
        # print(r.status_code,r.reason) #获取状态码,获取状态码的原因
        # print(r.headers)#响应头

        # print(type(r.text))
        # print(r.content) #byte,图片、文件，
        # print(type(r.content))
        # print(r.request.headers) #请求头
        # print(r.request.url)
        # print(r.request.method)
        # print(type(response))
        # print(response['headers']['Connection'])
        # print(eval(r.text)['headers']['Connection'])
