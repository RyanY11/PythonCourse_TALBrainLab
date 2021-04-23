# 第七讲

## os模块

当我们需要用Python对文件和路径进行操作时，会首先需要用到os模块

os模块下有非常多对文件的路径操作的函数，以下用几个常用的为例具体看看

### 获取当前工作目录
os.getcwd()

### 改变当前工作目录
os.chdir

### 创建文件目录（文件夹）
os.mkdir('dirname')

### 删除文件目录（文件夹）
os.rmdir('dirname')

### 列出指定目录下的所有文件和子目录
os.listdir('dirname')

### 删除文件
os.remove()

### 重命名文件
os.rename("oldname","newname")

### 一个目录树下的所有文件名
os.walk()
	# 使用os.walk扫描目录
	import os
	
	for curDir, dirs, files in os.walk("test"):
	    print("====================")
	    print("现在的目录：" + curDir)
	    print("该目录下包含的子目录：" + str(dirs))
	    print("该目录下包含的文件：" + str(files))

## os下的os.path模块

### 文件路径
os.path.dirname(path)

### 绝对路径
os.path.abspath(path)

### 文件名
os.path.basename(path)

### 路径拼合
os.path.join(path1[, path2[, ...]])

	os.path.join('C:\\Users\\TAL brainlab', 'Downloads','test.txt')

[其它os及os.path相关的函数](https://www.runoob.com/python3/python3-os-file-methods.html)

## 文件的读写

### 打开文件
open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError

open(file, mode='r')

注意：文件open()之后，一定在结尾需要有close()！

	open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

### 参数的说明
file: 必需，文件路径（相对或者绝对路径）

mode: 可选，文件打开模式

encoding: 一般使用utf8

newline: 区分换行符

### 几种常用的文件操作模式：
'x'  只新建文件

'b'  二进制模式

'r'  只读方式打开一个文件

'+'  打开一个文件进行更新(可读可写)

'r+'  打开文件用于读写

'w'  打开文件只用于写入（如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除；如果该文件不存在，创建新文件）

'w+'  打开文件用于读写（如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除；如果该文件不存在，创建新文件）

'a'  打开文件用于追加（如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后；如果该文件不存在，创建新文件进行写入）

'a+'  打开文件用于读写（如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后；如果该文件不存在，创建新文件进行写入）

试试仅写入，使用write(方法)：

	# 例1 创建一个文本文件并写入

	f = open("test.txt", "w")
	f.write('This a test of file writing.')
	f.close()

试试在只读取模式下写入：

	# 例2 用read()方法读取刚才写入的文件

	f = open("test.txt", "r")
	neirong = f.read()
	print(neirong)
	f.write('Something else.')
	f.close()

感受一下写入和追加的区别：

	# 例3 试一下a+和w+的区别

	# f = open("test.txt", "w+")
	# f.write('\n')
	# f.write('Something new.')
	# f.close()

	f = open("test.txt", "a+")
	f.write('\n')
	f.write('Something new.')
	f.close()

还有一种写入方法是按行写入，使用writelines方法：

	# 例4 使用writelines按行写入

	f = open("test1.txt", "w")
	# seq = ['line1', 'line2', 'line3']
	seq = ['line1\n', 'line2\n', 'line3\n']
	f.writelines(seq)
	f.close()

其实和write没有太大区别，只是writeline接收的是一个数组

注意：换行通过换行符'\n'实现

与写入相似的是，文件可以直接用read()读取，也可以用readlines读取：

	# 例5 按行读取readlines

	f = open("test1.txt", "r+")
	neirong = f.readlines()
	print(neirong)
	f.close()

## CSV文件的读取和写入

首先需要

	import csv

### 单行和多行写入

	# 例6 单行与多行写入csv文件

	import csv

	headers = ['class','name','sex','height','year']
	rows = [
	        [1,'xiaoming','male',168,23],
	        [1,'xiaohong','female',162,22],
	        [2,'xiaozhang','female',163,21],
	        [2,'xiaoli','male',158,21]
	    ]

	with open('test.csv','w',newline='')as f:
	    f_csv = csv.writer(f)
	    f_csv.writerow(headers)
	    f_csv.writerows(rows)

### 读取

	# 例7 读取csv

	import csv
	with open('test.csv')as f:
	    neirong = csv.reader(f)
	    for row in neirong:
	        print(row)

需要查看固定的某一行，只需要改为row[行标]

## Let us try try
请自定义一个函数，在电脑的某个目录下创建文件夹”测试数据“，并创建“第一批”，“第二批”，“第三批”三个子文件夹，每个子文件夹中都有一个ReadMe.txt文件，写一点简单的文字描述，另一个文件是一个csv数据表，随便写几个数据就可以。