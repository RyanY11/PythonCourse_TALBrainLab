# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:19:43 2021

@author: TAL brainlab
"""

# 例5 按行读取readlines

f = open("test1.txt", "r+")
neirong = f.readlines()
print(neirong)
f.close()