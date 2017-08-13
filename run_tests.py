#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:jinzj
@contact:
@others:
@desc:
"""
import time, sys, os
sys.path.append('./test_case')
sys.path.append('./public')
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
from public import mail

def send_email(filename):
    mail_host='smtp.exmail.qq.com'
    mail_user=mail.mail_user   #邮箱名 '2837065966@qq.com'
    mail_pass=mail.mail_pass   #密码 ；'#￥%……'

    sender=mail.sender  #发送邮箱名
    receivers=['2837065966@qq.com'] #收件人

    message=MIMEMultipart('related')

    f=open(filename,'rb')
    mail_body=f.read()
    att = MIMEText(mail_body,'base64','uft-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att)
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    message.attach(msg)
    message['From']=sender
    message['To'] =  ",".join(receivers)
    message['Subject']=Header("接口自动化测试报告",'utf-8')
    smtp=smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receivers,message.as_string())
    smtp.quit()

def report(testreport): #查找最新的测试报告
    lists = os.listdir(testreport)  #返回指定的文件夹包含的文件或文件夹的名字的列表
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))#通过sort()方法重新按时间对目录下的文件进行排序
    filename = os.path.join(testreport, lists[-1])#list[-1]取最新生成的文件或者文件夹
    print(filename)
    return filename


if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据
    # 指定测试用例为当前文件夹下的 test_case 目录
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='qiaoba testing Interface Test Report',
                            description='The results are following:')
    runner.run(discover)
    fp.close()

    test_report = './report' #定义报告文件目录
    rep = report(test_report)
    send_email(rep)
