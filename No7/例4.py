# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:11:57 2021

@author: TAL brainlab
"""

# 例4 使用writelines按行写入

f = open("test1.txt", "w")
# seq = ['line1', 'line2', 'line3']
seq = ['line1\n', 'line2\n', 'line3\n']
f.writelines(seq)
f.close()