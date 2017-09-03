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
        # count.add = mock.Mock(name='add', return_value=7)
        # count.add = mock.Mock(return_value=count.add2(2, 3))
        count.add = mock.Mock(return_value = 7,side_effect=count.add2)
        result = count.add(8,5)
        print(result)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()
