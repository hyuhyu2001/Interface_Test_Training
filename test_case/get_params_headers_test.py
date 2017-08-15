#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:有params和headers
"""

import unittest
from public import base

testcasefile = 'get_params_headers_test_data.xlsx'
AllData =  base.get_data(testcasefile,'AllData')
TestData = base.get_data(testcasefile,'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
DataAll = TestData[1][1]
Expectedresult = TestData[1][2]

class GetParamsHeadersTest(unittest.TestCase):
    '''GET有params和headers测试'''
    def setUp(self):
        endpoint = EndPoint
        self.url = base.get_url(endpoint)

    def test_params_headers(self):
        '''验证浏览器是否Chrome'''
        '''给服务器发送请求'''
        DataALL = eval(DataAll)
        Method = RequestMethod
        resp = base.get_response(self.url,Method,**DataALL)

        User_Agent = resp['headers']['User-Agent']
        self.assertIn(Expectedresult,User_Agent)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()



