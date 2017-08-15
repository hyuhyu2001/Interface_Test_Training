#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:读取excel操作
"""

import os
import xlrd
from datetime import date,datetime

newpath = os.chdir(r'D:\python_pycharmWorkspace\python36\Interface_Test_Training\test_case\excel_train')
filename = "100G测试资源（视频+教程）免费获取.xlsx"
file = os.path.join(os.getcwd(),filename)

'''一、打开文件'''
xl = xlrd.open_workbook(file) #打开excel

'''二、获取sheet'''
print(xl.sheet_names())#获取所有sheet的名字
print(xl.nsheets)
print(xl.sheets())
print(xl.sheet_by_name('目录')) #通过名称获取
print(xl.sheet_by_index(1)) #通过索引获取

'''三、获取sheet内的汇总数据'''
table1 = xl.sheet_by_name('目录')
print(table1.name) #获取sheet的名称
print(table1.nrows)  #获取总行数
print(table1.ncols)  #获取总列数

'''四、单元格批量读取'''
print(table1.row_values(0)) #返回包含第1行值的列表，注意合并单元格，只能取第1个的值，其他为空
print(table1.row(0))
print((table1.row_types(0)))
print(table1.row_values(1))#返回包含第2行值的列表
print(table1.row_values(1,0,2))#返回包含第2行,包含第1列和第2列的值
print(table1.row_slice(1,0,2)) #list   [text:'QQ群号', number:205089395]
print(table1.row_types(1,0,2))  # <class 'array.array'>  array('B', [1, 2])

print(table1.col_values(1,0,2))#返回包含第2列,包含第1行和第2行的值
print(table1.col_values(0)) #返回包含第1列值的列表，注意合并单元格，只能取第1个的值，其他为空
print(table1.col_values(2)) #返回包含第3列值的列表

'''五、特定单元格读取'''
print(table1.cell(1,2).value)#获取第2行，第3列单元格的值
print(table1.cell_value(1,2))
print(table1.row(1)[2])
print(table1.row(1)[2].value)
print(table1.row(1)[2].ctype)

'''六、常用技巧：(0,0)转换成A1'''
print(xlrd.cellname(0,0)) #A1  cellname方法把一对行和列索引转换为一个对应的Excel单元格引用
print(xlrd.cellnameabs(0,0)) #$A$1 cellnameabs方法把一对行和列索引转换为一个绝对的Excel单元格引用（如：$A$1）
print(xlrd.colname(0)) #A  colname方法把一个列索引转换为Excel列名

'''七、获取表格内不同类型的name'''
def read_excel(table,row,col):
    name = table.cell_value(row,col)
    ctype = table.cell_type(row,col)
    if ctype == 0:
        name = "''"
    elif ctype == 1:
        name = name
    elif ctype == 2 and name % 1 == 0:
        name =  int(name)
    elif ctype == 3:
        '''方法一'''
        date_value = xlrd.xldate_as_tuple(name,0) #转换为元组形式 (2017, 11, 11, 0, 0, 0)
        # name = date(*date_value[:3]).strftime('%Y/%m/%d') #date_value[:3]为(2017, 11, 11) *date_value[:3]为 2017 11 11
        name = datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S') #datetime指日期时间，date只是至日期
        # name = time.strftime("%Y-%m-%d %H:%M:%S", date_value) #time模块也可以，但需要元组传递9个值，目前只有6个
        '''方法二'''
        # date_value = datetime(*xlrd.xldate_as_tuple(name, 0)) #date
        # name = date_value.strftime('%Y/%d/%m %H:%M:%S')
        '''方法三'''
        # date_value = xlrd.xldate.xldate_as_datetime(name, 0)  # 直接转化为datetime对象
        # name = date_value
    elif ctype == 4:
        name = True if name == 1 else False
    return name

#ctype : 0 empty, 1 string,  2 number,  3 date,  4 boolean,  5 error
# 5 error 这是由xlrd.XL_CELL_ERROR常数表示的。这种单元格的值是表示特定错误代码的整数。error_text_from_code方法用来把错误代码转换为错误信息
# print(table1.cell_type(1,0))  #返回1，字符串
print(table1.cell_value(1,0))
print(read_excel(table1,1,0))
# print(table1.cell_type(1,1))  #返回2，数字
print(table1.cell_value(1,1))
print(read_excel(table1,1,1))
# print(table1.cell_type(0,1))  #返回0，empty
print(table1.cell_value(0,1))
print(read_excel(table1,0,1))
# print(table1.cell_type(0,7)) #返回3，日期
print(table1.cell_value(0,7))
print(read_excel(table1,0,7))
# print(table1.cell_type(0,8)) #返回4，布尔，0位false，1为True
print(table1.cell_value(0,8))
print(read_excel(table1,0,8))
