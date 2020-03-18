from sympy import *
from sympy.abc import*

x, y = symbols('x y')

print(cos(x).rewrite(sin))  #выразить одну функцию через другую
print(cos(x).rewrite(exp))

print(trigsimp(cos(x)*cos(y) + sin(x)*sin(y))) #упрощение тригонометрии
print(expand_trig(sin(3*x)))    #разложение тригонометрии

# то же самое есть для логарифма, обязательно учесть область определения
a, b = symbols('a b', positive=True)
l = expand_log(log(a*b**3))
print(l)
l = logcombine(l)
print(l)

f = sin(x) + y**2
print(f.subs([(x, tan(y)), (y, cos(x))])) #подстанока
print(f.subs([(x, tan(y)), (y, cos(x))], simultaneous=True))    #одновременная подстановка

f = sin(x)**3 + sin(x) + log(x) + x*exp(y)
print(f.replace(sin(x), cos(x)))    #замена
print(f.replace(sin(x)**3, cos(x)))

mc = series(exp(x), x, 0, 5) #ряд Тейлора в точке 0 до 5 члена
print(mc)
print(diff(mc))
print(mc.subs(x, 0))
mc = mc.removeO()     #чтобы можно было подставить x (для консоли)
print(mc.subs(x, 5))


#ПРОИЗВОДНЫЕ
f = sin(x + 2*y)
print(diff(f, x))   #производная по х
print(diff(f, x, 2))    #производная 2 порядка
print(diff(f, x, 2, y, 3))  #производная 2 порядка по х и 3 порядка по у
print(Derivative(f, x))     #производная в невычесленном виде. Derivative - d/dx
print(Derivative(f, x).doit())

h = symbols('h', cls=Function)
g = x + h(x)
print(diff(g, x))


#ИНТЕГРАЛЫ
print(integrate(sin(x), x)) #неопределенный интеграл
print(integrate(exp(x), (x, 0, 5)))    #определенный интеграл
print(integrate(sin(x+y), (x, 0, pi/2), (y, 0, pi)))    #кратный интеграл
print(Integral(sin(x), x))
print(Integral(sin(x), x).doit())

#ПРЕДЕЛЫ
print(limit((1+1/x)**x, x, oo))
print(limit(log(x), x, 1, dir='+'))     #односторонний предел
print(limit(x**2, x, oo))

# СУММА РЯДА
print(summation(1/i**6, (i, 1, oo)))
