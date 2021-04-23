# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:39:33 2021

@author: TAL brainlab
"""

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x) #这里用append()函数，意思是追加元素
    l.sort()
print(l)