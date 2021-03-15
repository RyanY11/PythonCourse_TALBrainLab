# 第五讲

## 看看大家都写了什么有意思的小功能

分享一下我的“午饭吃啥？”

	# 例1 午饭吃啥？
	import random

	finish = False
	choice = []

	while finish == False:
    	try:
        	n = int(input("今天吃饭有几个选项："))
        	for i in range(n):
            	option = input("请输入第 %s个选项：" %str(i+1))
            	choice.append(option)
        
        	r = random.randint(0, n-1)
        	print("这样吧，今天午饭吃 " + choice[r] + "去")
        	finish = True
        
    	except ValueError:
        	print("输入的选项数不正确，请重新输入！")

当我们需要站在前人的肩膀上解决问题的时候，试试搜索一下相关的包，然后import它们就好了！

扩展：
[Python中对字符串的操作](https://www.runoob.com/python/python-strings.html)

## 函数 function

Python内置函数：input(), print(), range(), len()……

我们也可以自己将需要重复使用的一段小功能的代码，写为自定义函数。

特点：有规律、可重复，实现一次编写，多次调用

核心：抽象！将不变的东西放进函数，变的东西作为该函数的入参

### 定义函数

	def <function name> (agruments):
		return <result>

通过函数名，参数及返回值去定义一个函数

	# 例2 成年计算器

	def chengnian(age):
	    if age >= 18:
	        return "已成年"
	    else:
	        return "未成年"

	print(chengnian(17))

return表示从函数中往外传递出的参数，不return，函数执行完毕之后只能看到None

	# 例3 成年计算器

	def chengnian(age):
	    if age >= 18:
	        True
	        #return "已成年"
	    else:
	        False
	        #return "未成年"

	print(chengnian(17))

注意：return之后的语句将不会被执行

### 通过添加错误处理的模块，来完善我们自定义的函数

	# 例4 成年计算器升级版

	def chengnian(age):
	    if not isinstance(age, (int, float)):
	        raise ValueError('Cannot calculate your age because it seems not a integer or float')
	    if age >= 18:
	        return "已成年"
	    else:
	        return "未成年"

	print(chengnian('1'))

打开No.4作业中大家自己写的代码，我们一起将其改造成一个函数

### 关于函数的调用

我们前面的例4现在被保存在agejudge.py文件中，我们通过import去调用它，来完成另一个功能

	# 例5 函数的调用

	from agejudge import chengnian

	namelist = [{'name':'张三','age':20}, {'name':'李四','age':16}]

	for i in range(len(namelist)):
	    namelist[i]['ageType'] = chengnian(namelist[i]['age'])

	print(namelist)

通过抽象和调用的操作，事情是不是变得简洁了？可读性也得到了增强。

想一想，今天涉及的内容与工程化和组块化，有什么关系？

## Let us try try
请使用def构建一个或几个自定义函数，然后通过import将它（们）引用到一段代码中，用于实现某个小功能或者小玩法，命名后上传到大家的GitHub