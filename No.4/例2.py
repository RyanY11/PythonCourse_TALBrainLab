# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:30:31 2021

@author: TAL brainlab
"""

# 例2：条件语句的嵌套用法

num = input("请输入一个数字：")
if num.isnumeric() is True:
    if num >= 5:
        print("大的数")
    elif num < 5:
        print("小的数")
    else:
        print('你在搞事情') 
elif num.isalpha() is True:
    print('让你输入数字，你输入字母干嘛？')
else:
    print('输什么乱七八糟的了？') 