#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc：写入excel操作
"""
import datetime
import xlsxwriter

'''一、创建一个excel文件，创建sheet'''
workbook = xlsxwriter.Workbook('test.xlsx') #打开会清空数据
worksheet = workbook.add_worksheet('test')

'''二、特定单元格写入数据'''
#1、文本
worksheet.write('A1','巧吧软件测试')
worksheet.write(1,0,'xlsx') #等同于A2

#1.1、设置行单元格属性
worksheet.set_row(0,40)
#1.2、设置列单元格属性
worksheet.set_column('A:F',20)
#1.3、自定义格式写入
top = workbook.add_format({'border':1,'font_size':13,'bold':True,'align':'center','bg_color':'cccccc'})
worksheet.write('A3','巧吧软件测试',top)
# worksheet.set_row(0,40,top)
# worksheet.set_column('A:F',20,top)

#2、数字
worksheet.write(0,1,32)
worksheet.write(1,1,35.5)
#3、函数
worksheet.write(2,1,'=sum(C1:C2)')

#4、日期
worksheet.write(0,2,datetime.datetime.strptime('2017-11-11','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))

#5、图片
worksheet.insert_image(0,4,'巧吧软件测试.jpg')
worksheet.insert_image(0,3,'巧吧软件测试.jpg',{'url':'http://www.baidu.com','x_scale':0.2, 'y_scale':0.2})

#6、批量写入列
worksheet.write_column('A22',[1,2,3,4])
#批量写入行
worksheet.write_row('A21',[5,6,7,8],top)

#7、合并单元格写入
worksheet.merge_range(4,0,5,2,'巧吧软件测试',top) #开始行，开始列，终止行，终止列

workbook.close()
