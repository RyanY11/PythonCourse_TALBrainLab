# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:16:31 2021

@author: TAL brainlab
"""

# 例1
import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(1,11) 
y =  2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()