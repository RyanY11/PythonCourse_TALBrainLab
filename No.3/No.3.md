# 第二讲 原材料篇（上）

## 变量 variables

Python不用像其它语言一样，需要提前声明变量和类型，直接赋值就可以使用

### 整型 integer

int  整数，可以有正负

    a = 3

### 浮点型 float

float  小数，可以有正负

    b = -3.14

### 字符型 string

str  任何类型的字符

    c = "π"

### 布尔型 bool

bool  只有True和False

    d = False

### 空型 none

NoneType  python中特殊的数据类型，表示“没有”本身

    e = None

### 变量命名规范

Camel 命名法（驼峰命名法）：混合使用大小写字母来构成变量和函数的名字

    myVar = 1
    MyOwnVar = -1

下划线命名法：字母、数字或单词之间用下划线_连接

    my_var = 2
    my_own_var = -2

### 变量类型查看&转换

    type()

    int()
    str()
    float()

## 运算

### 加法

    5 + 3

### 减法

    7 - 10

### 乘法

    3 * 4

### 除法
观察两种除法的区别

    6 / 3
    6 // 3
猜一下，这个是什么？

    11 % 2

### 乘方

    2 ** 3

## 数据结构

### list 列表
list中的元素item，不需要是同样的数据类型

    f = [4,5,6]
    g = ['a',3,True]

list的索引
索引值以 0 为开始值，-1 为从末尾的开始位置

    g[1]
    g[-2]

list的修改

    g[0] = 'test'
    g[1:2] = []

list的截取

	gg = [1,2,3,4,5,6]
    gg[1:4:2]

list的连接

    g + gg

### dictionary 字典
反映的是映射关键，包含键与键值的配对

    h = {"name": "Alan","age": 24}

dict的查询

    h['name']

dict的添加

    h['height'] = 178

### tuple 元组
与list很像，但是元组一旦被设定便不能再更改

    i = ('abcd', 786, 2.23, 70.2)

tuple的索引与截取与list相同

## 常用的对数据类型的操作

### 长度查询

    len()

### 打印

    print()

## 回顾
变量：integer float string bool none

计算：加 减 乘 除 平方

数据类型：list dictionary tuple

from 字母 to 词