#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:side_effect指定的参数值为一个list或者tuple
到这里想起了python中的生成器函数，yield的用法有点像return，返回的是一个生成器函数，
当调用这个函数的时候，写在函数中的代码并没有真正执行，他只是返回了一个生成器。
"""

from mock import Mock

fooList = [100,200,300]
mockFoo = Mock(return_value=50,side_effect=fooList)
mockObj = mockFoo()
print(mockObj) #100
mockObj = mockFoo()
print(mockObj) #200
mockObj = mockFoo()
print(mockObj)#300
mockObj = mockFoo()
print(mockObj)#报错