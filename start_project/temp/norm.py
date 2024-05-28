import matplotlib.pyplot as plt
from matplotlib.patches import Circle
# from sympy import *
import numpy as np

a = np.linspace(-2,2,101)

X,Y = np.meshgrid(a,a)

# 分解 公式
# Z1 = np.abs(X) ** 2 + np.abs(Y) ** 2
# Z2 = np.abs(X) + np.abs(Y)
# fig,ax = plt.subplots()
# ax.plot(a,np.sqrt(np.abs(4-(np.abs(a)**2))))
# ax.set_aspect('equal',adjustable = 'box')
# plt.show()


# l2范数
# fig,ax = plt.subplots(subplot_kw = {'projection': '3d'})

# ax.contour(X,Y,Z2,levels = 2)
# ax.set_xlim(X.min(),X.max())
# ax.set_ylim(Y.min(),Y.max())
# ax.set_zlim(Z2.min(),Z2.max())
# ax.set_xticks([X.min(),X.max()])
# ax.set_yticks([Y.min(),Y.max()])
# ax.set_zticks([Z2.min(),Z2.max()])
# plt.show()

# 向量
a = np.array([3,2])
b = np.array([1,2])
c = a + b
fig,ax = plt.subplots(1,2)

ax[0].quiver(0,0,a[0],a[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'r',width = 0.0025)
ax[0].quiver(0,0,b[0],b[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'r',width = 0.0025)
ax[0].quiver(0,0,c[0],c[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'r',width = 0.0025)
ax[0].set_xlim(-5,5)
ax[0].set_ylim(-5,5)
ax[0].set_xticks([-5,5])
ax[0].set_yticks([-5,5])
ax[0].set_aspect('equal')
ax[0].spines[['left','bottom']].set_position('zero')
ax[0].spines[['right','top']].set_visible(False)

circle = Circle((0,0),radius = 1,edgecolor = 'black',facecolor = None,fill = False)
cosine = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

ax[1].quiver(0,0,a[0],a[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'b',width = 0.0015)
ax[1].quiver(0,0,b[0],b[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'b',width = 0.0015)
# ax[1].quiver(0,0,c[0],c[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'b',width = 0.0015)

a = a / np.linalg.norm(a)
b = b / np.linalg.norm(b)
# c = c / np.linalg.norm(c)

ax[1].quiver(0,0,a[0],a[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'r',width = 0.0025)
ax[1].quiver(0,0,b[0],b[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'r',width = 0.0025)
# ax[1].quiver(0,0,c[0],c[1],angles = 'xy',scale_units = 'xy',scale = 1,color = 'r',width = 0.0025)
ax[1].add_patch(circle)

print(np.dot(a,b),cosine)

ax[1].set_xlim(-5,5)
ax[1].set_ylim(-5,5)
ax[1].set_xticks([-5,5])
ax[1].set_yticks([-5,5])
ax[1].set_aspect('equal')
ax[1].spines[['left','bottom']].set_position('zero')
ax[1].spines[['right','top']].set_visible(False)
ax[1].annotate(f'{np.arccos(np.dot(a,b)):.2f}.2f',xy = (0,0),xytext=(0.01, .99),size=0.25)
plt.show()

print(cosine * np.linalg.norm(a) * np.linalg.norm(b))
