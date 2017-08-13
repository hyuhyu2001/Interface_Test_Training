#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:索引和列名相互转换
"""
import os
import xlrd

def get_table(newpath,filename,sheet_name):
    file = os.path.join(os.getcwd(), filename)
    xl = xlrd.open_workbook(file)
    table = xl.sheet_by_name(sheet_name)
    return table

'''Excel列名转换为索引'''
def colname_to_num(colname):
    if type(colname) is not str:
        return colname
    # print(len(colname))
    col = 0
    power  = 1
    for i in range(len(colname) - 1, -1, -1):
        ch = colname[i]
        col += (ord(ch) - ord('A') +  1 ) * power
        power *= 26
        # print(i)
    return col - 1

'''索引转换为Excel列名'''
def colnum_to_name(colnum):
    if type(colnum) != int:
        return colnum
    if colnum > 25:
        ch1 = chr(colnum % 26 + 65) #取余数
        ch2 = chr(colnum // 26 + 64) #取整数,/是精确除法，//是向下取整除法，%是求模（取余）
        return ch2 + ch1
    else:
        return chr(colnum % 26 + 65)



'''返回包含第row行,包含第col_start列和第col_end列的值'''
def  row_values_custom(table,row,col_start,col_end):
    col_start = colname_to_num(col_start)
    col_end = colname_to_num(col_end)
    return table.row_values(row-1,col_start,col_end+1)

'''返回包含第col列,包含第row_start行和第row_end行的值'''
def  col_values_custom(table,col,row_start,row_end):
    col = colname_to_num(col)
    return table.col_values(col,row_start-1,row_end)

'''返回包含第col列,包含第row_start行和第row_end行的值'''
def cell_value(table,col,row_start,row_end):
    z = col.upper()
    data = [table.cell(i, colname_to_num(col) - colname_to_num('A')).value for i in range(row_start -1, row_end )]
    return data

if __name__ == "__main__":
    a =colname_to_num("B")
    b = colnum_to_name(28)
    newpath = os.chdir(r'D:\python_pycharmWorkspace\python36\Interface_Test_Training\test_case\excel_train')
    filename = "100G测试资源（视频+教程）免费获取.xlsx"
    sheet_name = '目录'

    table = get_table(newpath,filename,sheet_name)
    print(row_values_custom(table,2,'A','B'))#返回包含第2行,包含第1列和第2列的值
    print(col_values_custom(table,'B',1,2))#返回包含第2行,包含第1列和第2列的值
    print(cell_value(table,'F',2,5)) #F2-F5里的数据转换为列

    # data = [table.cell(i, ord('F') - ord('A')).value for i in range(1, 9)]
    # print(ord('G'))  # 70
    # print(ord('A'))  # 65
