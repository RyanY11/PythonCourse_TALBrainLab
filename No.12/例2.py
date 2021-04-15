# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 例 2

import time  # 设置爬虫等待时间
import requests  # 获取网页数据
from bs4 import BeautifulSoup  # 解析网页数据
import csv

# 获取豆瓣网址并解析数据
def get_douban_books(url, num):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    res = requests.get(url, headers=headers)  # requests发起请求，静态网页用get
    soup = BeautifulSoup(res.text, 'html.parser')

    item_a_title = soup.find_all("td", class_="title")
    for item in item_a_title:
        tag_a = item.find("a")
        name = tag_a["title"]
        link = tag_a["href"]

        # TODO 第一种方式：排除不想租的位置或者某些条件（例如位置，钱数，例如：八通线，2700）
        # not_contains = ["八通线", "天通苑", "宋家庄", "龙泽", "后沙峪", "亦庄", "密云", "房山", "通州",
        #                 "石景山",
        #                 "2700", "2800", "2900", "3000", "3100", "3200", "3300", "3300", "3400"]
        
        # flag = False
        # for nc in not_contains:
        #     if nc in name:
        #         flag = True
        # if not flag:
        #     # print("[{}]({})".format(name, link))
        #     csv_writer.writerow([name, link])

        # TODO 第二种方式：添加想租的位置或者某些条件（例如位置，钱数，例如：八通线，2700）
        contains = ["西北旺" "中关村", "健德门", "惠新西街南口", "四号线", "十号线", "4号线",
                    "10号线", "1分钟", "2分钟", "3分钟", "4分钟", "5分钟"]
        for c in contains:
            if c in name:
                csv_writer.writerow([name, link])


# 定义保存CSV的位置
f = open('D:\\TAL\\内部学习\\Python2021\\No12爬虫基础及GUI介绍\\豆瓣北京租房信息.csv','w',encoding='utf-8-sig',newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['租房信息', '链接地址'])  # 表头

# 填写需要获取的页数
# all_page = 1
all_page = int(input("请填写需要获取的页数："))
# 每页个数
page_size = 30
url = 'https://www.douban.com/group/beijingzufang/discussion?start={}'
urls = [url.format(num * page_size) for num in range(all_page)]
page_num = [num * page_size + 1 for num in range(all_page)]
for i in range(all_page):
    get_douban_books(urls[i], page_num[i])
    print("==========第" + str(i + 1) + "页，完成==========")
    # 暂停 1 秒防止访问太快被封
    time.sleep(1)

# 保存 CSV 文件
f.close()
print("写入完成！")