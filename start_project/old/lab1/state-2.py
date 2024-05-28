# python字符使用unicode编码来表示文本
# unicode编码的格式是前缀\u或者\U
print("\u00c6")
# 使用子符用\N{name}
print("\N{cat}")

# 在磁盘中所有对象都是以二进制数字(0和1表示)这8个为一组，为1字节
# python中提供来两种字节数组：不可变bytes和可变bytearray

# 不可变字节数组创建 直接创建使用前缀加b方式 不是字符串
bytes=b'hello word'
print(bytes)

print("\u00c6".encode("utf-8"))

# 可变字节数组创建方式
x=bytearray(b"hello")
# 不能直接替换 x[1]=b"o" 而要通过ord方法来替换
x[1]=ord(b'c')
print(x)

