# 第四讲 原材料篇（下）

before we start...

一切为了可读性服务，请务必养成写注释的好习惯！！！
> “#” 单行注释
> 
> ‘‘‘或“““ 多行注释

一般在整个代码开头通过注释描述整个代码是做什么的，有哪些情况需要说明的

再在每个小模块和一些关键行之前，说明功能，变量和目的等信息

## 条件

Python条件语句是通过一条或多条语句的执行结果（True或者False，或者可以理解为是或否）来决定执行的代码块

### 基本结构

	if condition_1:
		statement_block_1
	elif condition_2:
		statement_block_2
	else:
		statement_block_3

注意：缩进！！！！

### 关系判断

	小于 <
	小于等于 <=
	等于 == 
	>= 大于等于
	> 大于
	!= 不等于

注意：“=”是赋值，与关系判断无关

### 例1

    num = input("请输入一个大于0小于4的数字：")
    # 判断num的值，3 2 1 0 和其它
    if num == '3':
    	print('boss')
    elif num == '2':
    	print('leader')
    elif num == '1':
    	print('worker')
    elif num == '0':
    	print('user')
    else:
    	print('你在搞事情') 

### 例2

	# 例2：条件语句的嵌套用法

	num = input("请输入一个数字：")
	if num.isnumeric() is True:
		if num >= 5:
			print("大的数")
		elif num < 5:
			print("小的数")
		else:
			print('你在搞事情') 
	elif num.isalpha() is True:
		print('让你输入数字，你输入字母干嘛？')
	else:
		print('输什么乱七八糟的了？') 

## 循环

### while循环

#### 基本结构

	while 判断条件(condition)：
    	执行语句(statements)……

只要condition成立，就执行statements，直到condition不成立

	#例3 while循环用法

	count = 0

	while (count < 9):
		print('The count is:', count)
		count += 1

	print("Goodbye!")

#### continue和break

continue 语句跳出本次循环，break 语句跳出整个循环

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

#### 将while循环和if条件判断放到一起

	# 例5 while下嵌套if的用法
	number = 7
	guess = -1
	print("数字猜谜游戏!")
	while guess != number:
		# 获取用户输入并转化为integer
		guess = int(input("请输入你猜的数字："))
 
		if guess == number:
			print("恭喜，你猜对了！")
		elif guess < number:
			print("猜的数字小了...")
		elif guess > number:
			print("猜的数字大了...")
		else:
			print("unknown error...")

### for循环

for循环可以遍历任何序列的项目

#### 基本结构

	for <variable> in <sequence>:
		<statements>
	(else:
		<statements>)

一个for循环会通过一个variable去遍历一个sequence一定的次数，每次执行一遍statement

	# 例6 for循环用法

	languages = ["C++", "C#", "R", "Python"] 
	for x in languages:
		print (x)

	b = {'name':'Ted','age':24}
	for j in b.keys():
		print(j, b[j])

#### range()函数

使用range()函数返回一个数列的值，在for循环中很常用

	range(5)
	range(2,5)
	range(1,5,2)
	range(5,0,-1)
	range(4,-1,-1)

参数：range(start，stop，step)

	for i in range(1,5):
		print(i)

#### len()函数

len()函数返回对象（字符、列表、元组等）长度或项目个数，在for循环中很常用

	# 例7 组合使用range和len函数

	a = ['Google', 'Baidu', 'TAL', 'Tencent', 'ByteDance']
	for i in range(len(a)):
		print(i, a[i])

## 错误和异常的处理

### 错误类型

> AttributeError：属性错误，特性引用和赋值失败时会引发属性错误
> 
> NameError：试图访问的变量名不存在
> 
> SyntaxError：语法错误，代码形式错误
> 
> IOError：一般常见于打开不存在文件时会引发IOError错误，也可以解理为输出输入错误
> 
> KeyError：使用了映射中不存在的关键字（键）时引发的关键字错误
> 
> IndexError：索引错误，使用的索引不存在，常索引超出序列范围，什么是索引
> 
> TypeError：类型错误，内建操作或是函数应于在了错误类型的对象时会引发类型错误
> 
> ZeroDivisonError：除数为0，在用除法操作时，第二个参数为0时引发了该错误
> 
> ValueError：值错误，传给对象的参数类型不正确，像是给int()函数传入了字符串数据类型的参数。

#### 语法错误 SyntaxError

常见于缩进、括号、冒号、引号、=或==、使用了python关键字做变量名等情况

注意观察报错时，SyntaxError: invalid syntax指向的箭头位置，做对应修改

#### 对异常的处理

try/except 语句基本结构

	try：
		<statements>
	except <error type>:
		<do something to hanle this error>

尝试执行statements，当出现某类错误时，通过执行另外的语句来处理这样的错误，而不是直接导致程序的退出

	#例8 对例5的代码添加异常值处理功能
	number = 7
	guess = -1
	print("数字猜谜游戏!")
	while guess != number:
		try:
			# 获取用户输入并转化为integer
			guess = int(input("请输入你猜的数字："))
 
			if guess == number:
				 print("恭喜，你猜对了！")
			elif guess < number:
				print("猜的数字小了...")
			elif guess > number:
				print("猜的数字大了...")
			else:
				print("unknown error...")
			except ValueError:
				print("您输入的不是数字，请再次尝试输入！")

> try/except...else
> 
> else 子句将在 try 子句没有发生任何异常的时候执行
> 
> try-finally 
> 
> finally 子句无论是否发生异常都将执行最后的代码

### Let us try try

一个小作业

请使用条件判断，循环和异常值处理相关的内容，写一段简单的代码，实现某个小功能或者小玩法，命名后上传到大家的GitHub
