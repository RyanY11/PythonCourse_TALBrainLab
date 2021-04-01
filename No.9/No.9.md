# 第九讲 matplotlib

终于，我们来到了人民群众喜闻乐见的数据可视化部分，这里讲一个很常用的数据可视化工具包matplotlib

[https://matplotlib.org/](https://matplotlib.org/)

## 基础入门
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

## 线图入门教程

[https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py](https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)

## 一些各式各样的图

[https://matplotlib.org/stable/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py](https://matplotlib.org/stable/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py)

## 完整tutorial
[https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)

## Let us try try