from sympy import *
from sympy.abc import *     #позволяет не определять ряд переменных


f = (x**2 -1)/(x**4-1)
pprint(apart(f))        #красивая печать
print(gcd(10, 5))
print(lcm(2, 6))
print(factorint(20))    # множители
print(isprime(19134702400093278081449423917))   #простота числа

pprint(sympify("x**2 + 5*x + 6"))
print(nsimplify(0.33, tolerance=0.01))