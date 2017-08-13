#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:Requests 允许你使用自己指定的身份验证机制
"""
import requests

#basic
r = requests .get('http://httpbin.org/basic-auth/user/passwd',auth = ('user','passwd'))
print(r.text)

#方法2
from  requests.auth import HTTPBasicAuth
r1 =  requests .get('http://httpbin.org/basic-auth/user/passwd',auth = HTTPBasicAuth('user','passwd'))
print(r1.text)

#Digest
from  requests.auth import HTTPDigestAuth
r2 =  requests .get('http://httpbin.org/digest-auth/auth/user/passwd/MD5',auth = HTTPDigestAuth('user','passwd'))
print(r2.text)


#Oauth
headers = {'Authorization':'token dd6322fa6c57a548268453dcdsadfcdc352a7811'}
response = requests.get(url,headers = headers)

#自定义身份验证
requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
