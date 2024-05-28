import numpy as np
from sympy import *

print(bin(ord('X')))

a = np.array([3,4])
b = np.array([4,3])
print("模长计算:",np.linalg.norm(a))

x,y = symbols('x,y')
a = Matrix([cos(x),sin(x)])
b = Matrix([cos(y),sin(y)])
print("点积结果:",a.dot(b))
print("化简:",trigsimp(a.dot(b)))
