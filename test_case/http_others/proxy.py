#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:代理：代理 URL 必须包含连接方式。
"""
import requests

#1、使用代理
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
requests.get("http://example.org", proxies=proxies)

#2、可以设置环境变量
# $ export HTTP_PROXY="http://10.10.1.10:3128"
# $ export HTTPS_PROXY="http://10.10.1.10:1080"
# $ python
# requests.get("http://example.org")

#3、若你的代理需要使用HTTP Basic Auth，可以使用 http://user:password@host/ 语法
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}

#4、要为某个特定的连接方式或者主机设置代理，使用 scheme://hostname 作为 key， 它会针对指定的主机和连接方式进行匹配。
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}

#5、SOCKS
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}

