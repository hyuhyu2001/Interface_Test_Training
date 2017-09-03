#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc: patch创建类的构造器：return_value，side_effect
"""

import sys
import unittest
from unittest import mock
sys.path.append('./mock_train')
import modular

'''一、mock一个函数'''
# class TestCount2(unittest.TestCase):
#
#     @mock.patch("modular.add_def")
#     def test_add(self,mock_add):
#         mock_add.return_value = 7  #patch，return_value设置
#         mock_add.side_effect = modular.add_def2 #patch，side_effect设置
#         result = modular.add_def(8,5)
#         print(result)
#         self.assertEqual(result,13)

'''一、mock对象里的一个方法'''
class TestCount2(unittest.TestCase):
    # def setUp(self):
    #     self.count = modular.Count()
    @mock.patch.object(modular.Count,"add")
    def test_add(self,mock_add):
        count = modular.Count()
        mock_add.return_value = 7
        mock_add.side_effect = count.add2
        result = count.add(8,5)
        print(result)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()
