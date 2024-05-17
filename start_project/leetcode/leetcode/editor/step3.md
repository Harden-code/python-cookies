1. 栈的定义
- 先进后出,后进先出
- 栈是一种操作受限的线性表,只允许在一端(栈顶)插入和删除数据

2. 队列的定义
- 先进先出,后进后出
- 队列是一种操作受限的线性表,只能队列头部取数据,尾部插入数据

基于数组循环队列
head,tail

# python deque
#  d[0]  peek at rightmost item
#  d[-1] peek at leftmost item
# stack append(Add x to the right side of the deque.)
#       pop(Remove and return an element from the right side of the deque.)
#      
# queue append(Add x to the right side of the deque.)
#       popleft(Remove and return an element from the left side of the deque)
