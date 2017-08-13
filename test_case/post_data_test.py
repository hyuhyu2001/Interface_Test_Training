#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:编码为表单形式的数据,通过data参数传递
"""


#第1步：导入模块
import unittest
from public import base
from public import HttpService

#第2步：必须继承unittest.TestCase
class PostDataTest(unittest.TestCase):
    '''Post，data测试'''

    # 第3步：主要是配置环境：进行测试前的初始化工作，比如在接口测试前面做一些前置的参数赋值，数据库操作等等
    def setUp(self):
        endpoint = 'post'
        self.url = base.get_url(endpoint)

    # 第4步：定义测试用例，名字以“test”开头
    def test_post_data_1(self):
        '''form值验证'''
        params = {'show_env':1}
        data = {'a':'巧吧软件测试','b':'form-data'}

        DataALL = {'params':params,'data':data}
        Method = 'post'
        resp = base.get_response(self.url,Method,**DataALL)

        form = resp.get('form').get('a')

        # 第5步：定义assert断言，判断测试结果
        self.assertEqual(form,'巧吧软件测试')

    #@unittest.skip('无条件跳过')
    def test_post_data_2(self):
        '''form值type类型判断'''
        params = {'show_env':1}
        data = {'a':'巧吧软件测试','b':'form-data'}

        DataALL = {'params':params,'data':data}
        Method = 'post'
        resp = base.get_response(self.url,Method,**DataALL)
        form = resp.get('form').get('a')

        self.assertEqual(form,'巧吧软件测试')
        self.assertIsInstance(form,str)

    # 第6步：清理环境：测试后的清除工作，比如参数还原或销毁，数据库的还原恢复等
    def tearDown(self):
        pass

if __name__ == "__main__":
    # 第7步：调用unittest.main()启动测试
    unittest.main()








