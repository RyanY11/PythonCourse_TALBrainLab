# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:28:52 2021

@author: TAL brainlab
"""

# 例4 continue 和 break 用法

print("continue example:")

i = 1
while i < 10:   
    i += 1
    # 非双数时跳过输出
    if i%2 > 0: 
        continue
    # 输出双数2、4、6、8、10
    print(i)

print("break example:")

i = 1
# 循环条件为1必定成立
while 1:
    # 输出1~5
    print(i)
    i += 1
    # 当i大于5时跳出循环
    if i > 5:
        break