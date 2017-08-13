#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     巧吧软件测试
@desc:cookies
"""
import requests

host = 'http://httpbin.org/'
endpoint = 'cookies'
url = ''.join([host,endpoint])
url1 = 'http://www.baidu.com/'

'''给服务器发送请求'''
r = requests.get(url)
print(r.cookies)  #获取cookies
print(r.text)
d = requests.utils.dict_from_cookiejar(r.cookies) #jar包转换为字典
print(d)
print({a.name:a.value for a in r.cookies})

#发送cookies至服务器
cookies = {'cookie-name':'qiaoba'}
r1 = requests.get(url,cookies = cookies)
print(r1.text)

#复杂的写法
s = requests.Session()
c = requests.cookies.RequestsCookieJar()
c.set('cookis-name','cookie-value',path = '/',domain = '.test.com')
s.cookies.update(c)
print(s.cookies)
