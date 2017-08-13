#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:传递JSON格式的数据
"""

import unittest
from public import base

class PostJsonTest(unittest.TestCase):
    def setUp(self):
        endpoint = 'post'
        self.url = base.get_url(endpoint)

    def test_post_json(self):
        json = {
            "info": {"code": 1, "sex": "男", "id": 1900, "name": "巧吧软件测试"},
            "code": 1,
            "name": "巧吧软件测试", "sex": "女",
            "data": [{"code": 1, "sex": "男", "id": 1900, "name": "巧吧软件测试"}, {"code": 1, "sex": "女", "id": 1900, "name": "巧吧软件测试"}],
             "id": 1900
        }
        DataALL = {'json':json}
        Method = 'post'
        resp = base.get_response(self.url,Method,**DataALL)

        name = resp.get('data')
        self.assertIsInstance(name,str)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()




