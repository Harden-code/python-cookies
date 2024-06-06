import sympy
import numpy as np
from sympy import *

print(bin(ord('X')))

a = np.array([3, 4])
b = np.array([4, 3])
print("模长计算:", np.linalg.norm(a))

x, y = symbols('x,y')
a = Matrix([cos(x), sin(x)])
b = Matrix([cos(y), sin(y)])
print("点积结果:", a.dot(b))
print("化简:", trigsimp(a.dot(b)))


a = series(1/(1-x), x, n=10).removeO()
b = series(1/(1-x**2), x, n=10).removeO()
c = series(1/(1-x**5), x, n=10).removeO()

z = simplify(a*b*c)
pprint(z)

pprint(expand(z))
