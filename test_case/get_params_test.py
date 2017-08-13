#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:只有params，通过url传递参数
"""

import unittest
from public import base

class GetParams(unittest.TestCase):
    '''GetParams测试'''
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_url(endpoint)

    def test_get_params1(self):
        '''test_get_params1测试'''
        params = {'show_env':1}
        '''给服务器发送请求'''
        DataALL = {'params':params}
        Method = 'get'
        resp = base.get_response(self.url,Method,**DataALL)

        connect = resp.get('headers').get('Connection')
        self.assertEqual(connect,'close')

    def test_get_params2(self):
        '''test_get_params2测试'''
        params = {'show_env':1}
        '''给服务器发送请求'''
        DataALL = {'params':params}
        Method = 'get'
        resp = base.get_response(self.url,Method,**DataALL)

        connect = resp.get('headers').get('Connection')
        self.assertIsInstance(connect,str)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
