# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:05:46 2021

@author: TAL brainlab
"""

#例8 对例5的代码添加异常值处理功能
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    try:
        # 获取用户输入并转化为integer
        guess = int(input("请输入你猜的数字："))
 
        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")
        else:
            print("unknown error...")
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")