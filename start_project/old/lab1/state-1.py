# python中//向上取整数
i = 3 // 2
print(i)

# ** 是取平方
a = 3 ** 2
print(a)
# 输入函数
# name = input("what")
# print(name)

# 可以用手单引号或双引号来表示字符串
print("name")
print("let'go")
# print('let'go')
# 使用反斜杠\转意
print('let\'go')

print("\"hello\"")

# 拼接字符串 当且仅当连续输入两个字符串,可以自动拼接
str_ = " let's say "  "hello word"
print(str_)

# 字符串的表示 str和repr
# str可将值转换为用户能看懂的字符串 (会去除转意符号)
parse_str = "my name \nharden"
print(str(parse_str))
# repr会忽略转意符号,直接输出值
print(repr(parse_str))

# 长字符串 使用三引号表示 如果使用常规代码就需要换行直接在句末+\
print('''this is very long string,
it continues here,''')
print("his is very long string\
      it continues here")

# 原始字符串 比如window的dos系统使用c:\noname就会有奇异可以使用
print("c:\noname")
# 可以使用反斜杠来取消转意
print("c:\\noname")
# 如果使用很长的路径就会很烦,在自负暗沉前面加r也可以达到同样效果
print(r"c:\noname")

# 同样在路径的字符串中,末尾有\的字符串也会带来奇异
# print((r"c:\noname\"))
# 在末尾加\\也可以解决
print(r"c:\noname""\\")

