# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:40:11 2021

@author: TAL brainlab
"""

# 通过PyQt5制作一个租房搜索工具

import sys, os
from PyQt5.QtWidgets import (QWidget, QToolTip, QLabel, QLineEdit, QTextEdit, QGridLayout, QRadioButton,
     QTextBrowser, QFileDialog, QPushButton, QApplication)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont    
import time  # 设置爬虫等待时间
import requests  # 获取网页数据
from bs4 import BeautifulSoup  # 解析网页数据
import csv
from datetime import datetime  # 日期时间模块
 
#构造GUI类
class RentTool(QWidget):
    
    def __init__(self):
        super().__init__()
        # 初始化变量
        self.initUI()
        self.methodType = 1
        self.items = 0
        self.items_total = 0
        
    def initUI(self):
        #定义静态页面标签文字
        source = QLabel('检索源（默认豆瓣北京租房小组）：')
        method = QLabel('检索方式（正选/反选）：')
        keywords = QLabel('检索关键词（用英文逗号,分隔）：')
        num = QLabel('单页检索条数（默认检索全部30条）：')
        pages = QLabel('总检索页数：')
        location = QLabel('结果文件保存地址：')
        states = QLabel('状态：')

        #定义输入框
        self.sourceEdit = QLineEdit('https://www.douban.com/group/beijingzufang/discussion?start=0')
        self.keywordsEdit = QLineEdit()
        self.numEdit = QLineEdit('30')
        self.pagesEdit = QLineEdit('1')
        self.locationEdit = QLineEdit(os.getcwd())
        self.statesEdit = QTextBrowser()

        #这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        
        #创建单选按钮
        btn1 = QRadioButton('包含关键词')
        btn1.toggled.connect(lambda:self.btnstate(btn1))
        btn2 = QRadioButton('排除关键词')
        btn2.toggled.connect(lambda:self.btnstate(btn2))

        #创建一个PushButton并为他设置一个tooltip
        openloacation = QPushButton('选择文件夹', self)
        openloacation.clicked.connect(self.path)
        openloacation.setToolTip('选择保存结果CSV文件地址')

        #创建开始和退出按钮
        start = QPushButton('开始', self)
        start.clicked.connect(self.getContent)
        finish = QPushButton('退出', self)
        finish.clicked.connect(QCoreApplication.quit)

        #grid布局管理
        grid = QGridLayout()
        grid.setSpacing(15)

        grid.addWidget(source,1,0)
        grid.addWidget(self.sourceEdit,1,1,1,3)
        grid.addWidget(method,2,0)
        grid.addWidget(btn1,2,1)
        grid.addWidget(btn2,2,2)
        grid.addWidget(keywords,3,0)
        grid.addWidget(self.keywordsEdit,4,0,1,4)
        grid.addWidget(num,5,0)
        grid.addWidget(self.numEdit,5,1)
        grid.addWidget(pages,5,2)
        grid.addWidget(self.pagesEdit,5,3)
        grid.addWidget(location,6,0)
        grid.addWidget(self.locationEdit,6,1,1,2)
        grid.addWidget(openloacation,6,3)
        grid.addWidget(states,7,0)
        grid.addWidget(self.statesEdit,8,0,6,4)
        grid.addWidget(start,15,2)
        grid.addWidget(finish,15,3)

        self.setLayout(grid) 
        
        self.setWindowTitle('豆瓣租房搜索小工具')    
        self.show()

    #为单选构造选中函数    
    def btnstate(self,btn):
        #print(btn.text() + " is selected" )
        self.output_print('选中了：' + btn.text() + '模式！')
        if btn.text() == '包含关键词':
            self.methodType = 1
        else:
            self.methodType = 2
        
    #依据用户选择切换文件存储路径
    def path(self):
        directory = QFileDialog.getExistingDirectory()
        print(directory)
        self.output_print('文件保存至：' + directory)
        self.locationEdit.setText(directory)
        os.chdir(directory)

    #定义模块用于在状态区实时输出内容
    def output_print(self, msg):
        self.statesEdit.append(msg)
        self.cursor = self.statesEdit.textCursor()
        self.statesEdit.moveCursor(self.cursor.End)  #光标移到最后，这样就会自动显示出来
        QApplication.processEvents()

    #定义爬虫核心模块
    def get_info(self, url, type):
        """
        url为传入的爬虫爬取页面地址
        type切换使用包含关键词模式爬取或排除关键词模式爬取
        """
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
        
            #使用包含关键词
            if type == 1:
                for c in self.keys:
                        if c in name:
                            self.items += 1
                            self.items_total += 1
                            self.csv_writer.writerow([self.items_total, name, link])
            #使用排除关键词
            else:
                flag = False
                for nc in self.keys:
                    if nc in name:
                        flag = True
                    if not flag:
                        print("[{}]({})".format(name, link))
                        self.items += 1
                        self.items_total += 1
                        self.csv_writer.writerow([self.items_total, name, link])

    #获取用户输入并执行爬虫模块
    def getContent(self):
        self.output_print('检索时间：' + str(datetime.now()))
        self.output_print("开始检索……")
        self.output_print("  ")

        #获取关键词并转存为list
        content = str(self.keywordsEdit.text())
        self.keys = content.split(",")
        print(self.keys)

        # 获取的页数
        all_page = int(self.pagesEdit.text())
        
        # 获取的每页个数
        page_size = int(self.numEdit.text())
        #print(page_size)

        # 定义保存CSV的位置
        dt = datetime.now().strftime('%Y%m%d_%H%M')
        filename = '租房信息检索结果_%s.csv' % (dt)
        f = open(filename,'w',encoding='utf-8-sig',newline="")
        self.csv_writer = csv.writer(f)
        # 构造表头
        self.csv_writer.writerow(['编号', '租房信息标题', '链接地址'])

        url = str(self.sourceEdit.text())
        newurl = url.replace('=0', '={}')
        #print(newurl)
        urls = [newurl.format(num * page_size) for num in range(all_page)]
        #print(urls)
        #print(self.methodType)

        page_num = [num * page_size + 1 for num in range(all_page)]
        #print(page_num)
        for i in range(all_page):
            self.items = 0
            self.get_info(url=urls[i], type=self.methodType)
            msg = "============第" + str(i + 1) + "页，检索完成, 写入" + str(self.items) + "条============"
            print(msg)
            self.output_print(msg)

            # 暂停 1.5秒防止访问太快被封
            time.sleep(1.5)

        # 保存 CSV 文件
        f.close()
        print("写入完成！")
        self.output_print("共" + str(self.items_total) + "条信息被写入文件。")
        self.output_print("检索结果保存成功！")
        self.output_print("  ")

#运行类
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rt = RentTool()
    sys.exit(app.exec_())