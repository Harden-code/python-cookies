from math import pi

# 根据格式设置宽度
# 10代编前面空格
print('{num:10}'.format(num = 3))
# .2f代表小数点后2位 对应其他类型也可截取保留
print('pi day is {pi:.2f}'.format(pi=3.13245))
print('{:.5}'.format('guido van'))
# 直接在值后面加数字就是设置的宽度
print('pi day is {pi:10.2f}'.format(pi=3.13245))

#千分位表示
# 同时指定其他格式设置元素时,都好应该放在宽度和和表示精度的语句之间
print('{:,}'.format(10**10))
# 在字符串有10个字符 其多余的用0填充
print('{:010.2f}'.format(pi))
# ** 代表间隔 :后面是格式 个数
print('{:0.2f}'.format(pi**10))
# 指定左对齐 右对齐 和居中分别用< > ^
print('{:<10.2f}'.format(pi))
print('{:>10.2f}'.format(pi))
# 10代表10个字符长度
print('{:^10.2f}'.format(pi))
# 对齐符号放在设置长度之前
print('{:&^10.2f}'.format(pi))