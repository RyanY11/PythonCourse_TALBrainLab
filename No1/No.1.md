# 课前·锅和锅铲的配备 #
### Python安装版本 ###
Python3.7.9

下载链接：[https://www.python.org/downloads/release/python-379/](https://www.python.org/downloads/release/python-379/ "Python3.7.9")

### Mac下的安装

点击下载 macOS 64-bit installer，运行 python-3.7.9-macosx10.9.pkg

### Windows下的安装
点击下载 Windows x86-64 executable installer，运行python-3.7.9-amd64.exe

###高级·通过包管理工具安装Python环境
推荐：Anaconda

[anaconda.com](anaconda.com "Anaconda官网")

[https://www.jianshu.com/p/62f155eb6ac5](https://www.jianshu.com/p/62f155eb6ac5 "Anaconda介绍、安装及使用教程")

### 确认是否安装成功
terminal 或 cmd 输入 Python 并回车

返回显示Python版本信息后，即安装成功

### IDE
- Visual Studio
- PyCharm
- Eclipse
- Jupyter Notebook
- Spyder
- Sublime text

本次课程推荐使用Spyder

原因：安装Python后自带，轻量，好用

### 配备好了锅和锅铲，把玩把玩吧

1. Hello world

`print("hello world!")`

2. 输入三个整数，然后由大到小排列后输出

> l = []  
> for i in range(3):  
> x = int(input('integer:\n'))  
> l.append(x) #这里用append()函数，意思是追加元素  
> l.sort()  
> print(l)

打开IDE并运行try1.py