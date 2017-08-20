#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:xlutils修改excel
"""

import xlrd
import xlutils.copy
# import xlutils.compat

xl = xlrd.open_workbook('test.xlsx') #打开文件,低版本设置formatting_info=True复制格式，高版本已经不支持

workbook = xlutils.copy.copy(xl)  #复制xl文件

worksheet = workbook.get_sheet(0) #通过get_sheet()获取的sheet有write()方法

worksheet.write(0,0,'changed') #修改操作

workbook.save(r'xlutils_save.xls')#只能复制内容，不能复制格式，且不能保存为xlsx文件