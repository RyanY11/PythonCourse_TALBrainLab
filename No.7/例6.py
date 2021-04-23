# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:52:39 2021

@author: TAL brainlab
"""

# 例6 单行与多行写入csv文件

import csv

headers = ['class','name','sex','height','year']
rows = [
        [1,'xiaoming','male',168,23],
        [1,'xiaohong','female',162,22],
        [2,'xiaozhang','female',163,21],
        [2,'xiaoli','male',158,21]
    ]

with open('test.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)