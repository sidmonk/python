from sympy import *

x, y = symbols('x y')
exuation = Eq(E**x, 5) #уравнение
ans = solve(exuation, x)    #решить относительно x
print(ans)

# CИСТЕМА УРАВНЕНИЙ
print(solve((x + y - 5, x + 2), (x, y)))
print(solve_linear_system(Matrix([[1, 1, 5], [1, 0, -2]]), x, y))


#ДИФФУРЫ
t = symbols('t')
x = symbols('x', cls=Function)
dif_exuation = Eq(diff(x(t), t) + x(t), 5)
ans = dsolve(dif_exuation, x(t))
#ЗАДАЧА КОШИ x(0) = 0
C1 = symbols('C1')
C1_0 = solve(Eq(ans.rhs.subs(t, 0), 0), C1)
print(C1_0)
ans = ans.rhs.subs(C1, C1_0[0])
print(ans)

