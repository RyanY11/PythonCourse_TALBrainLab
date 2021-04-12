# 第十一讲 re

是否还记得我们在前面讲次中讲的例子，对获取到的用户输入进行判断？
我们之前用的方法是什么样的？

是不是可以有一些更高级的方法，去实现更加精准的字符串匹配、查找、替换？

正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

[https://www.runoob.com/python/python-reg-expressions.html](https://www.runoob.com/python/python-reg-expressions.html)

[https://www.jb51.net/article/65286.htm](https://www.jb51.net/article/65286.htm)

[https://docs.python.org/zh-cn/3.8/library/re.html](https://docs.python.org/zh-cn/3.8/library/re.html)

在讲正则之前先补充一点点关于字符串格式化的内容

## f-string 格式化

[http://www.python3.vip/tut/py/basic/10/#f-string-%E6%A0%BC%E5%BC%8F%E5%8C%96](http://www.python3.vip/tut/py/basic/10/#f-string-%E6%A0%BC%E5%BC%8F%E5%8C%96)

## 正则表达式入门介绍

[http://www.python3.vip/tut/py/extra/regex/](http://www.python3.vip/tut/py/extra/regex/)

[https://www.bilibili.com/video/BV1q4411y7Zh?from=search&seid=89204275837223941](https://www.bilibili.com/video/BV1q4411y7Zh?from=search&seid=89204275837223941)

### 在线验证工具
[https://regex101.com/](https://regex101.com/)

### 常用函数
re.match  单次从开始匹配

re.search  单次全匹配

（re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配）

re.sub  替换

re.compile  生成正则表达式对象，用于匹配或搜索

re.findall  多次全匹配，返回字符串

re.finditer  多次全匹配，返回迭代器

re.split  将匹配的字符串分隔后返回列表

[https://www.runoob.com/python/python-reg-expressions.html](https://www.runoob.com/python/python-reg-expressions.html)