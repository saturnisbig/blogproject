#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
导入身份证属地数据
"""
import xlrd
import sys

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'blogproject.settings')

import django
django.setup()

from tool.models import CardID

data = xlrd.open_workbook('./cardplace.xlsx')
# 第一个表
sheet1 = data.sheet_by_index(0)
# print sheet1.nrows, sheet1.ncols
nrows = sheet1.nrows
ncols = sheet1.ncols
# 表头数据
first_row_data = sheet1.row_values(0)
# print row_data
for i in range(1, nrows):
    row_data = sheet1.row_values(i)
    card = CardID.objects.create(number=str(int(row_data[0])),
                                 place=row_data[1])
    # for j in range(0, ncols):
    #     if j == 0:
    #         row_data[j] = int(row_data[j])

    #     print row_data[j],
    # print
    # if i == 5:
    #     break
