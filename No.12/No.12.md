# 第十二讲 爬虫&GUI

##爬虫

当我们需要快速、批量、结构化的从网站获取信息的时候，就是爬虫大显身手的场景。

[https://www.cnblogs.com/Albert-Lee/](https://www.cnblogs.com/Albert-Lee/)

### 理解网页&爬虫的基本原理

[http://c.biancheng.net/view/2011.html](http://c.biancheng.net/view/2011.html)

### 通过requests库模拟网页请求

[https://www.cnblogs.com/Albert-Lee/p/6230337.html](https://www.cnblogs.com/Albert-Lee/p/6230337.html)

	# 例1 通过get方法获取网页信息

	import requests        #导入requests包
	url = 'https://www.cnblogs.com/Albert-Lee/p/6226699.html'
	strhtml = requests.get(url)        #Get方式获取网页数据
	print(strhtml.text)

## 使用beautiful soup提取网页信息

[https://www.cnblogs.com/Albert-Lee/p/6232745.html](https://www.cnblogs.com/Albert-Lee/p/6232745.html)

[https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)

## 通过爬虫爬取豆瓣租房信息

豆瓣北京租房小组
[https://www.douban.com/group/beijingzufang/discussion?start=25](https://www.douban.com/group/beijingzufang/discussion)

爬虫代码来源
[https://blog.csdn.net/weixin_40375601/article/details/109237806](https://blog.csdn.net/weixin_40375601/article/details/109237806)

修改后的租房信息爬虫见文件  例2.py

## Python下常用的GUI

GUI - Graphical User Interface

### tkinter
Python自带的标准GUI库，简洁直接
[https://www.runoob.com/python/python-gui-tkinter.html](https://www.runoob.com/python/python-gui-tkinter.html)

[https://docs.python.org/zh-cn/3/library/tkinter.html](https://docs.python.org/zh-cn/3/library/tkinter.html)

	# 例3 tkinter示例

	import tkinter as tk

	class Application(tk.Frame):
	    def __init__(self, master=None):
	        super().__init__(master)
	        self.master = master
	        self.pack()
	        self.create_widgets()

	    def create_widgets(self):
	        self.hi_there = tk.Button(self)
	        self.hi_there["text"] = "Hello World\n(click me)"
	        self.hi_there["command"] = self.say_hi
	        self.hi_there.pack(side="top")

	        self.quit = tk.Button(self, text="QUIT", fg="red",
	                              	command=self.master.destroy)
	        self.quit.pack(side="bottom")

	    def say_hi(self):
	        print("hi there, everyone!")

	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

### wxPython
Python 对跨平台的 GUI 工具集 wxWidgets （ C++ 编写）的包装，常见的tk替代品
[https://www.wxpython.org/](https://www.wxpython.org/)

wxPython示例见文件  例4.py

### PyQt5
功能强大，界面漂亮，跨平台支持优秀
[https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

[http://code.py40.com/face](http://code.py40.com/face)

PyQt5示例见文件  例5.py

## Let us try try
尝试使用爬虫和GUI制作一个小工具，点击开始爬取内容，并存储到文件