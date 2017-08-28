#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc: mysql常用方法培训
"""

import pymysql
from public import Config

'''一、创建连接和游标'''
conn = pymysql.connect(**Config.sql_conn_dict)
# cur = conn.cursor() #虽然拿到了python的数据库连接， 但是不能在这个对象上直接对数据库进行操作， 还需要获取对应的操作游标才能进行数据库的操作
# 创建游标以字典的类型
cur = conn.cursor(cursor=pymysql.cursors.DictCursor) #fetch返回内容不同，一个是返回元组，字典形式是返回字典

'''二、查询'''
'''查询，无参数的情况'''
sql = 'SELECT * FROM student '
cur.execute(sql)  # 执行sql，并返回受到的影响行数
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchmany(2))
print(cur.fetchall())
'''查询，有一个参数的情况'''
code = 1
sql = "SELECT * FROM student where code = %s" %code
cur.execute(sql)
sql = "SELECT * FROM student where code = %s"
cur.execute(sql,code) #这种方式 更清晰一些， 安全性也更好， 能有效防止sql注入
print(cur.fetchall())
'''查询，1个参数有多个值的情况'''
code = ('1','2','3') #['1','2','3']
sql = "SELECT * FROM student where code = %s"
cur.executemany(sql,code)
print(cur.fetchall())
'''查询，多个参数多个值的情况'''
code = [['women','18'],['man','25']] #(('women','18'),('man','25'))
sql = "SELECT * FROM student WHERE sex = %s AND age = %s"
cur.executemany(sql,code)  #这种方式 更清晰一些， 安全性也更好， 能有效防止sql注入
print(cur.fetchall())

'''三、增删改'''
'''增删改，有一个参数的情况，commit'''
sql = "UPDATE student SET NAME = '巧吧' WHERE sex = 'women' and age = '18'"
cur.execute(sql)
conn.commit()
'''增删改，多个参数的情况，commit()'''
code = [['women','18'],['man','19']]
sql = "UPDATE student SET NAME = '巧吧软件测试' WHERE sex = %s and age = %s"
cur.executemany(sql,code)
conn.commit()
'''增删改，一个成功，一个失败的情况，rollback()'''
sql1 = "UPDATE student SET NAME = '巧吧软件测试1' WHERE sex = 'women' and age = '18'"
sql2 = "UPDATE student SET NAME = '巧吧软件测试巧吧软件测试' WHERE sex = 'man' and age = '19'"
try:
    cur.execute(sql1)
    cur.execute(sql2)
    conn.commit()
    print('', True)
except Exception as e:
    conn.rollback()
    print(e, False)
'''四、关闭游标和连接'''
cur.close()
conn.close()