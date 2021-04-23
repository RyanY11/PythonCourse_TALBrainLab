# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:50:26 2021

@author: TAL brainlab
"""

# 例2 用read()方法读取刚才写入的文件

f = open("test.txt", "r")

neirong = f.read()
print(neirong)
f.write('Something else.')
f.close()