#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc: 类的构造器：return_value，side_effect
"""

import unittest
from unittest import mock
from .modular import *

class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        # count = mock.Mock(name='add', return_value=7)
        # count.add = mock.Mock(return_value=count.add2(2, 3))
        count.add = mock.Mock(return_value = 7,side_effect=count.add2)
        # count.add.configure_mock(return_value = 8) #configure_mock修改return_value值
        # # count.add = mock.Mock() 如果没有指定的属性，则在configure_mock中添加属性
        # count.add.configure_mock(side_effect=count.add3)
        result = count.add(8,5)
        count.add.assert_called_with(8,5)

        count.add.assert_called_once_with(8,5)
        count.add(8,5)
        # count.add.assert_called_once_with(8,5) #第二次调用会报错

        count.add.assert_called_with(8,5)
        count.add(2,3)
        count.add.assert_called_with(2,3)
        # count.add.assert_called_with(8,5) #此处会报错，因为是仅检查最近一次的调用
        count.add.assert_any_call(8,5) #上次调用的是(2,3)，但曾经被调用过便可以
        param1 = mock.call(8,5)
        param2 = mock.call(2,3)
        callsList = [param1,param2]
        count.add.assert_has_calls(callsList,any_order = False) #any_order = False 必须顺序一致
        # count.add.assert_has_calls([param2,param1])
        count.add.assert_has_calls([param2,param1],any_order = True) #any_order = True忽略传入顺序T

        '''查看mock对象都有哪些属性'''
        # print(dir(mock.MagicMock()))

        # count.add.reset_mock()#恢复到mock之前的状态
        print(count.add.called) #返回mock对象所做的任意调用的访问器,如果后续没有函数调用mock，则返回false
        print(count.add.call_count)  #mock函数被调用的次数
        print(count.add.call_args) #获取工厂调用时的参数（最近使用的参数）
        print(count.add.call_args_list) #获取工厂调用的所有参数，是个列表
        print(count.add.method_calls)  # 测试一个mock对象都调用了哪些方法，返回是一个list
        print(count.add.mock_calls) #显示工厂调用和方法调用

        '''mock一个类，类去调用方法'''
        mockFoo = mock.Mock(spec=Count)
        mockFoo.add(1,1)
        mockFoo.add(1,2)
        print(mockFoo.method_calls)#测试一个mock对象都调用了哪些方法，返回是一个list
        print(mockFoo.mock_calls) #显示工厂调用和方法调用

        self.assertEqual(result,13)
if __name__ == '__main__':
    unittest.main()
