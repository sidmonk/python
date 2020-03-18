from sympy import *

x = symbols('x', integer=True, positive=True)
print(sqrt(x**2))

print(sqrt(2).n(2))

x, y = symbols('x y')
f = 3*x + 5*y - 7 + 15 - sin(pi/2)
print(f.subs([(y, sin(y)), (x, tan(x))]))       #подставить

print(S(1)/2 + S(2)/3)
print(Rational(4, 6) + Rational(10, 20))

print(sin(2*pi/3))   #символьно
print(sin(2*pi/3).evalf(3))     #с точностью до знаков

print(roots(x**2 + 2*x + 3, x))     #корни многочлена
print(real_roots(x**2 + 2*x + 3, x))    #действительные корни

z = symbols('z')
pol = expand((x+y+z)**2)    #раскрыть скобки
print(pol)
print(factor(pol))      #сгруппировасть

pol = (x**3 - y**3)/(x**2-y**2)
print(cancel(pol))      #сократить

pol = x/(x + y) + y/(y - x)
print(together(pol))  #к общему знаменателю

pol = (x**2 + y**2)/(x**2 - y**2)
print(apart(pol, x))  #на простые дроби