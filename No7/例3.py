# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:55:00 2021

@author: TAL brainlab
"""

# 例3 试一下a+和w+的区别

# f = open("test.txt", "w+")
# f.write('\n')
# f.write('Something new.')
# f.close()

f = open("test.txt", "a+")
f.write('\n')
f.write('Something new.')
f.close()