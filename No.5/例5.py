# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:27:52 2021

@author: TAL brainlab
"""

# 例5 函数的调用

from agejudge import chengnian

namelist = [{'name':'张三','age':20}, {'name':'李四','age':16}]

for i in range(len(namelist)):
    namelist[i]['ageType'] = chengnian(namelist[i]['age'])

print(namelist)