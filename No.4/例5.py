# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:05:40 2021

@author: TAL brainlab
"""
 
# 例5 while下嵌套if的用法
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
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