# 序列操作：索引,切片,相加,相乘和成员资格检查

# 索引 跟java类似都是从0开始计数，不同的是python可以使用负数作为索引
# 表示从右边开始往左数,-1代表左右一个
greeting = 'hello'
print(greeting[0])
print(greeting[-1])
print(greeting[-2])
# 对于字符串变量可以直接对其执行索引无需赋值
print('hello'[0])

# month = ['one', 'two', 'three', 'four', 'five']
# num = input("num:")
# print(month[int(num) - 1])

# 切片 用来访问特定范围内的元素

tag = '<a href="http://www.python.org">Python web site</a>'
# 第一个索引是包含第一个元素编号，第二表示切片后余下的第一个编号（左闭右开）
print(tag[9:30])
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[3:6])


# 技巧
# 访问最后三个元素
print(numbers[-3:-1])
# 第二个索引也可省略 直接切到末尾
print(numbers[-2:])

# 使用步长 通常切片忽略第三个参数,默认是1 代表每次移动1位
print(numbers[0::2])
# 另外步长不能为0否则不能移动,但可以为负数表示从右向左
print(numbers[-1::-2])
# 特殊（步长为负数，第一个索引必须比第二大-因为是从右到左）
print(numbers[7:2:-2])


# 序列相加
# 使用加法拼接序列
print([1,2,3]+[4,5])
# 使用乘法与数相乘时,将重复这个序列来创建一个新序列
print('python'*5)

# 空格序列初始化
seq=[None]*2
print(seq)

# 成员资格
# 使用in
print('i' in 'hihi')
print('c' in 'hihi')