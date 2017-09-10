#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""
from mock import Mock


# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        print("Foo:callFoo_")

    def doFoo(self, argValue):
        print("Foo:doFoo:input = ", argValue)

# create the first mock object
mockFoo = Mock(spec=Foo)
print(mockFoo)
# returns <Mock spec='Foo' id='507120'>
print(mockFoo.call_count)
# returns: 0

mockFoo()
print(mockFoo.call_count)
# returns: 1

mockFoo.callFoo()
print(mockFoo.call_count)
# returns: 1

mockFoo()
print(mockFoo.call_count)
# returns: 2