# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:00:01 2021

@author: TAL brainlab
"""

# 例1 通过get方法获取网页信息

import requests        #导入requests包
url = 'https://www.cnblogs.com/Albert-Lee/p/6226699.html'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)