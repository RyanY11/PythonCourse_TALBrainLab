# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:55:49 2021

@author: TAL brainlab
"""

# 例7 读取csv

import csv
with open('test.csv')as f:
    neirong = csv.reader(f)
    for row in neirong:
        print(row[1:3])
