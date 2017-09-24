#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:有params和headers
"""

import unittest
from public import base
from ddt import ddt,data,unpack

testcasefile = 'get_params_headers_test_data.xlsx'

AllData = base.get_data(testcasefile, 'AllData')
TestData = base.get_data(testcasefile, 'TestData')[1:]

@ddt
class GetParamsHeadersTest(unittest.TestCase):
    '''GET有params和headers测试'''
    def setUp(self):
        self.endpoint = AllData[1][1]
        self.RequestMethod = AllData[1][2]
        self.RequestData = AllData[1][3]
        self.url = base.get_url(self.endpoint)

    @data(*TestData)
    @unpack
    def test_params_headers(self,*TestData):
        '''验证浏览器是否Chrome'''
        '''给服务器发送请求'''
        Method = self.RequestMethod
        if self.RequestData != '':
            DataAll = eval(self.RequestData)
            resp = base.get_response(self.url,Method,**DataAll)
        else:
            resp = base.get_response(self.url, Method)

        User_Agent = resp[TestData[0]][TestData[1]]
        self.assertIn(TestData[2],User_Agent)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()



