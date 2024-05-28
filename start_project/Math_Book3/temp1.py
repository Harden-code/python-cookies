import matplotlib.pyplot as plt
import numpy as np
a = 1
b = 1

p = [0.5, 1, 2, 3]
q = p

pp, qq = np.meshgrid(p, q)
# flatten 扁平
pp = pp.flatten()
qq = qq.flatten()

x1 = np.linspace(-2, 2, num=101)
x2 = x1

xx1, xx2 = np.meshgrid(x1, x2)

fig, axes = plt.subplots(ncols=4, nrows=4, figsize=(12, 12))
# axes.flat
for p, q, ax in zip(pp, qq, axes.flat):
    if np.isinf(p):
        zz = np.maximum(np.abs(xx1/a), np.abs(xx2/b))
    else:
        zz = ((np.abs((xx1/a))**p)+(np.abs((xx2/b))**q))**(1./q)
        # zz=((np.abs((xx1/a))**p)+(np.abs((xx2/b))**q))

    ax.contourf(xx1, xx2, zz, 20, cmap='RdYlBu_r')
    ax.contour(xx1, xx2, zz, [1], colors='k', linewidths=2)

    ax.axvline(x=0, color='k', linewidth=0.25)
    ax.axhline(y=0, color='k', linewidth=0.25)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.spines['top'].set_visible = False
    ax.spines['bottom'].set_visible = False
    ax.spines['left'].set_visible = False
    ax.spines['right'].set_visible = False
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_title(f'p={str(p)},q={str(q)}')
    ax.set_aspect('equal', adjustable='box')
plt.show()
