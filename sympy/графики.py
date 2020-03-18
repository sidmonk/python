from sympy import *


from sympy.plotting import (plot_parametric, plot_implicit,
                            plot3d, plot3d_parametric_line,
                            plot3d_parametric_surface)
x = symbols('x')
plot(sin(x)/x, (x, -5, 5))

# фигура Лиссажу
t=Symbol('t')
plot_parametric(sin(2*t), cos(3*t), (t,-2*pi,2*pi),
                title='Lissajous', xlabel='x', ylabel='y')

# тор
u, v = symbols('u v')
a = 0.3
plot3d_parametric_surface((1+a*cos(u))*cos(v),
                          (1+a*cos(u))*sin(v),a*sin(u),
                          (u,0,2*pi),(v,0,2*pi))