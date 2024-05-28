from string import Template
from math import pi

# 标准序列的操作都适用于字符串的，但是字符串是不可变的因此不能对其进行切片赋值
website = 'http://www.python.org'
# website[-3:0]='com'

# 拼接字符串格式：在%左边指定一个字符串，在右边指定要设置值的格式
# 指定要设置其格式的值，可以用单个值可以用多个值
format = 'hello %s , James %s'
words = ('harden','word')
# % 是转换符说明符号,指出要将值插入什么地方，s意味着将值视为字符串格式设置
# 其他格式设置%3.f将格式设置为包含小数点后3位浮点数
print(format % words)

tmpl = Template('hello $who $what enough for ya')
print(tmpl.substitute(who = 'harden',what = 'dusty'))

print('{},{} and {}'.format('first','second','third'))
# 通过所以来定位替换
print('{2} {1} and {0}'.format('first','second','third'))
# 命名空间
# "{name} is {value:2.f}".format(name = "n",value = pi)

# 通过自动编号和手工编号转换
print('{foo} {} {bar} {}'.format(1,2,bar = 4,foo = 3))
# 使用列表
fullname=['james','harden']
print('mr {name[1]}'.format(name=fullname))

# 基本转换
print('the number is {num}'.format(num = 43).format())
# f是转为浮点类型
print('the number is {num:f}'.format(num = 43))
# b是转换为二进制
print('the number is {num:b}'.format(num = 43))