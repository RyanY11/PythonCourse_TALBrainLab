# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:51:03 2021

@author: TAL brainlab
"""

import numpy as np

# 例1 创建1维数组

np.array([1,2,3])  

np.arange(5)


# 例2 创建2维数组

np.array([[1, 2],  [3, 4]])


# 例3 创建3维数组

np.array([[1, 2, 3],  [4, 5, 6], [7, 8, 9]])
# 创建未初始化的数组
np.empty((2,2), dtype=int)
# 创建以0为元素的数组
np.zeros((2,2))
# 创建以1为元素的数组
np.ones([2,2])