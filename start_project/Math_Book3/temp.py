import matplotlib.pyplot as plt
from sympy import plot_implicit, symbols, Eq
x1, x2 = symbols('x1,x2')

# curve 曲线


def plot_curve(Eq_expr):
    h_plot = plot_implicit(Eq_expr, (x1, -2.5, 2.5), (x2, -2.5, 2.5),
                           xlabel='$\it{x_1}$', ylabel='$\it{x_2}$')


# 清除所有
plt.close('all')

# circle
Eq_sym = Eq(x1**2 + x2**2, 1)
plot_curve(Eq_sym)
