import string
# string 模块下的常量
# 0-9字符串
print(string.digits)

# 包含所有asc字符
print(string.ascii_letters)
# 小写asc字符串
print(string.ascii_lowercase)
# 可打印asc字符串
print(string.printable)
# asc标点字符的字符串
print(string.punctuation)
# 所有大些asc字母的字符串
print(string.ascii_uppercase)

# center 通过向两边填充字符让字符串居中
print('harden'.center(20))

# join合并元素 于split向反 (与java stream join)
seq=['1','2','3']
print('+'.join(seq))

# lower返回字符串小写版本 title首字母大写
print('HARDEN'.lower())
print('HARDEN'.lower().title())

# replace 替换
print('this is test'.replace('is','e'))

# strip 将字符串开头和末尾空白删除 lstrip rstrip
print('   harden  '.strip())
# 并且还可以指定符号
print('---harden--'.strip('-'))

# translate 与repalce一样是替换字符串,但不同的是它可以置换多个
# maketrans 第三个参数 还可以指定删除那些字符
table=str.maketrans('es','kz',' ')
print('this es test'.translate(table))

# 补充判断字符串满足特定条件
# isspace isdigit isupper 判断是否全是空白,数字,大写

