#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:多部分编码(Multipart-Encoded)的文件，files
    该方法只适用于上传小文件，上传大文件的时候就需要用到流式上传
"""

import requests

host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

# 1、普通上传
# files = {'files':open('test.txt','rb')}

#2、通过文件上传字符串等
# files = {'files':('test.txt','send ssss')}

#3、自定义文件名、文件类型以及请求头(请求文件名称、文件路径、文件类型、文件请求头)
# files = {'files':('巧吧软件测试.jpg',open('巧吧软件测试.jpg','rb'),'image/png')}

#4、传送多个文件
# files = [
#     ('field1',('test.txt',open('test.txt','rb'))),
#     ('field2',('巧吧软件测试.jpg',open('巧吧软件测试.jpg','rb'),'image/png'))
# ]

#5、流式上传
with open('test.txt') as f:
    r = requests.post(url,data=f)

print(r.headers)
print(r.text)

# resp =  r.json()
# print(resp['json'])