# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:43:18 2021

@author: TAL brainlab
"""

# 例1 创建一个文本文件并写入

f = open("test.txt", "w")

f.write('This a test of file writing.')

f.close()