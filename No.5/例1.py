# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:48:58 2021

@author: TAL brainlab
"""

# 例1 午饭吃啥？

import random

finish = False
choice = []

while finish == False:
    try:
        n = int(input("今天吃饭有几个选项："))
        for i in range(n):
            option = input("请输入第 %s个选项：" %str(i+1))
            choice.append(option)
        
        r = random.randint(0, n-1)
        print("这样吧，今天午饭吃 " + choice[r] + "去")
        finish = True
        
    except ValueError:
        print("输入的选项数不正确，请重新输入！")
