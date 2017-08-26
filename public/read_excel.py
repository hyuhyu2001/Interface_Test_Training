#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

import xlrd
#把excel中的参数值存入对应的字段
def save_data(ls,params=None,data=None,json=None,files=None):
    ls=ls[:-1]
    i=0
    if params!=None:
        for key in sorted(params.keys()):
            if ls[i]=='res':
                continue
            else:
                if params[key]=='arry':
                    params[key]=eval(ls[i])
                    i=i+1
                else:
                    params[key]=ls[i]
                    i=i+1
    if data!=None:
        for key in sorted(data.keys()):
            if ls[i]=='res':
                continue
            else:
                if data[key]=='arry':
                    data[key]=eval(ls[i])
                    i=i+1
                else:
                    data[key]=ls[i]
                    i=i+1
    if json!=None:
        if json=='arry':
            json=eval(ls[i])
        else:
            for key in sorted(json.keys()):
                if ls[i]=='res':
                    continue
                else:
                    if json[key]=='arry':
                        json[key]=eval(ls[i])
                        i=i+1
                    else:
                        json[key]=ls[i]
                        i=i+1
    if files=='':
        files=ls[i]
    elif files=='arry':
        files=eval(ls[i])
    return json

class XLDatainof(object):
    def __init__(self,path = ''):
        self.xl = xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheet_info(self):
        infolist = []
        for row in range(0,self.sheet.nrows):
            info = self.sheet.row_values(row)
            info = info[:-1]#20170825
            infolist.append(info)
        return infolist

if __name__ == "__main__":
    datainfo = XLDatainof(r'D:\python_pycharmWorkspace\python36\Interface_Test_Training\test_data\get_params_headers_test_data.xlsx')
    alldata = datainfo.get_sheetinfo_by_name('TestData')
    print(alldata)