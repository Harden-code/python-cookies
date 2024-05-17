# 字典推导
codes = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]

map_code = {key: value for key,value in codes}
print(map_code)


# 拆包
def dump(**kwargs):
    print('dump ',kwargs)
    return kwargs


# 可以多次使用** 进行拆包
dump(a = 2,b = 2,**{'c': 2,'d': 2})

# | 合并映射 求并集
d1 = {'a': 1,'b': 4,'d': 3}
d2 = {'a': 2,'b': 2,'c': 3}

# | 创建一个新的映射 |=更新现有的映射
print(d1 | d2)
d1 |= d2
print(d1)

# 当k存在时,d[k]抛出错误=>d.get(k,default);d[k]调用__getitem__,如果找不到就会调用__missing__


import heapq
# heapq.heappop()
