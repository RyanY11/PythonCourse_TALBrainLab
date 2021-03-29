# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:24:02 2021

@author: TAL brainlab
"""

# 例4 使用numpy解线性方程

import numpy as np 
 
a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
b = np.array([[6],[-4],[27]])

x = np.linalg.solve(a,b) 
print (x)