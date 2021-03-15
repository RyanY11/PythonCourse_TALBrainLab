# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:11:58 2021

@author: TAL brainlab
"""

# 例4 成年计算器升级版

def chengnian(age):
    if not isinstance(age, (int, float)):
        raise ValueError('Cannot calculate your age because it seems not a integer or float')
    if age >= 18:
        return "已成年"
    else:
        return "未成年"

#print(chengnian('1'))