# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:28:32 2021

@author: TAL brainlab
"""

# 例1：if,elif用法

num = input("请输入一个大于0小于4的数字：")
# 判断num的值，3 2 1 0 和其它
if num == '3':
    print('boss')        
elif num == '2':
    print('leader')
elif num == '1':
    print('worker')
elif num == '0':
    print('user')
else:
    print('你在搞事情') 