#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:有params和headers
"""

import unittest
from public import base
from public import HttpService

class GetParamsHeadersTest(unittest.TestCase):
    '''GET有params和headers测试'''
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_params_headers(self):
        '''验证浏览器是否Chrome'''
        params = {'show_env':1}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'}
        '''给服务器发送请求'''
        DataALL = {'params':params,'headers':headers}
        Method = 'get'
        resp = base.get_response(self.url,Method,**DataALL)

        User_Agent = resp['headers']['User-Agent']
        self.assertIn('Chrome',User_Agent)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()



