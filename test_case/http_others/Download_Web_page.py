#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:下载网页
"""

import requests

r = requests.get( 'http://www.baidu.com/')
with open('webtest.html','wb') as html:
    html.write(r.content)
html.close()