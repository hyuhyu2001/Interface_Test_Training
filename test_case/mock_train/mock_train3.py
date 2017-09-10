#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:spec
mockFoo1.attach_mock(mockFoo2,'fooBar')
mock_add_spec(aSpec， spec_set = False)
"""

from mock import Mock

'''一、spec指定的是属性组成的list'''
specList = ['_value','callfun1']
mockobj = Mock(spec=specList)
print(mockobj._value) #<Mock name='mock._value' id='50626000'>
print(mockobj.callfun1) #<Mock name='mock.callfun1' id='50626160'>
# print(mockobj.callfun2) #报错

'''二、spec指定一个类属性'''
class Foo1():
    def add1(self,a,b):
         return a + b
    def add2(self,a,b):
        return  a + b + 1

class Foo2():
    def add1(self,a,b):
         return a + b + 2
    def add2(self,a,b):
        return  a + b + 3

class Foo3():
    def add1(self, a, b):
        return a + b + 4

# mockFoo1 = Mock(spec=Foo1) #spec设置的是mock对象的属性，所以，这下，mock就有了3个属性了
mockFoo1 = Mock(spec=Foo1,return_value=Foo2())
print(mockFoo1)
mockFoo2 = Mock(spec=Foo2,return_value=Foo3())
# print(mockFoo2)

print(mockFoo1().add1(2,3))
print(mockFoo2().add1(2,3))
mockFoo1.attach_mock(mockFoo2,'fooBar')#将一个mock对象加到另一个mock对象中,命名为fooBar
# print(mockFoo1.fooBar)
# print(mockFoo1.fooBar.add1())
print(mockFoo1.fooBar().add1(2,3))

mockFoo3 = Mock(spec=Foo1)
print(mockFoo3.add2())
mockFoo3.mock_add_spec(Foo3) #向mock对象添加新的属性性(mock对象原来的属性就会被擦除),修改spec属性
# print(mockFoo3.add2())

def aa(a,b):
    return a*b
def aa2(a,b):
    return a*b*2

# mockFoo4 = Mock(spec=aa,return_value=aa2(1,2))
mockFoo4 = Mock(spec=aa,side_effect=aa2)
print(mockFoo4(1,2))
mockFoo4.mock_add_spec(aa2)
print(mockFoo4(1,2))

