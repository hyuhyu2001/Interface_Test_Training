#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

from mock import Mock,call


# The mock object
class Foo():
    # instance properties
    _fooValue = 123

    def callFoo(self):
        print("Foo:callFoo_")

    def doFoo(self, argValue):
        print("Foo:doFoo:input = ", argValue)

# create the first mock object
mockFoo = Mock(spec=Foo, return_value="narf")
# print(mockFoo.call_args)
# returns: None

print(mockFoo.doFoo("dfdfdf"))
print(type(mockFoo())) #<class 'str'>
# print(mockFoo.call_args)
# # returns: call('zort')
#
# mockFoo()
# print(mockFoo.call_args)
# # returns: call()
#
# mockFoo("troz")
# print(mockFoo.call_args)
# # returns: call('troz')
#
# mockFoo.callFoo()
# print(mockFoo.call_args)
# # returns: call('troz')