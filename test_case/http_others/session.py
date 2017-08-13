#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:会话对象:seeeion 是客户端与服务器之间的会话，用来保存用户的信息。
"""

import requests

host = 'http://httpbin.org/'
endpoint = 'cookies/set/sessioncookie/123456789'
url = ''.join([host,endpoint])
url1 = 'http://httpbin.org/cookies'

#发送请求
r = requests.get(url1)
print(r.text)

session = requests.Session() #初始化一个session对象
session.get(url) #cookies的信息存在了session中
r1 = session.get(url1)
print(r1.text)

header1 = {'test1':'aa'}
header2 = {'test2':'bb'}

session1 = requests.Session()
session1.headers.update(header1) #已经存在服务器中的信息
r2 = session1.get('http://httpbin.org/headers',headers = header2) #发送新的headers信息
print(r2.text)

session1.headers['test1'] = None #删除会话里的信息，赋值None即可
r3 = session1.get('http://httpbin.org/headers',headers = header2)
print(r3.text)

