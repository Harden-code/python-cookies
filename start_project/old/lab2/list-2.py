# 列表
# list 函数 其参数可以将任何序列作为list的参数（不仅仅是字符串）
str = list("hash")
print(str)
# 将list转换为字符串
print(''.join(str))

# 列表 增删改查
# 1 修改列表
x = [1, 2, 3]
x[1] = 5
print(x)
# 2 删除元素 下标位置
del x[2]
print(x)
# 3 切片
name = list('perl')
name[2:] = list('ar')
print(name)
name[1:] = list('ython')
print(name)
# 不替换原有元素情况下插入新元素
number = [1, 6]
number[1:1] = [2, 3, 4, 5]
print(number)
# 删除
number[1:] = []
print(number)

# 列表方法
# append 用于将一个对象附加到列表末尾
lst = [1, 2, 3]
lst.append(4)
# clear 清空列表 例如list[:]=[]
lst.clear()
# copy 复制列表 重新在内存开辟空间创建一个相同的链表
a = [1, 2, 3]
b = a
b[0] = 4
print(a, "vs", b)

c = a.copy()
c[0] = 6
print(a, 'vs', c)

# count 计算指定元素出现多少次
print(c.count(2))

# extend 同时将多个值附加到末尾 与+拼接的区别 +是创建一个全新的序列
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)

# index 在列表中找到第一个指定值的索引
names = ['harden', 'jony', 'jane']
print(names.index('harden'))

# insert用于一个对象插入列表
names.insert(2, '2')
# names[2:2]='2'
print(names)

# pop 从列表中删除一个元素,并返回（默认是最后一个）
# 另外python没有push 使用insert或者append来代替
x = [1, 2, 3]
print(x.pop())
# remove用于删除指定值的元素
x.remove(1)
print(x)

# reverse 反转列表
x = [1, 2, 3]
x.reverse()
print(x)

# sort 原地排序
x = [2, 1, 3]
x.sort()
# sorted返回一个新排序的链表
x = [2, 1, 3]
new = sorted(x)
print(new, 'v', x)
# 高级排序 sort可以接受两个参数key reverse
# key 相当于设置一个用于排序的的函数，在排序的时候用该函数来比较
words = ['123', '1', '1234']
words.sort(key=len)
print(words)
words.sort(key=len, reverse=True)

# 列表推导
nums = [x for x in range(10)]

for i in nums:
    print(i)