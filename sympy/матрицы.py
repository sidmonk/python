from sympy import *

# чтоб нормально печаталось
def mprint(M):
    maxlen = max([len(str(i)) for i in M])
    imax, jmax = M.shape
    print()
    print('\n'.join([''.join([str(M[i, j]).ljust(maxlen+1) for j in range(jmax)]) for i in range(imax)]))

M = Matrix([[i**j for j in range(4)] for i in range(4)])
print(M[0, 1])
mprint(M)
M1 = Matrix(4, 4, lambda i, j: i**j)    #можно так
mprint(M1)
print(M.shape)      #число строк и столбцов
mprint(M[2:, 2:])    #срез
mprint(M.reshape(2, 8))      #перетасовать
print(M.tolist())   #в список списков
mprint(M*M1)     #сразу можно умножать
mprint(M**(-1))    #обратная матрица
print(det(M))     #определитель

v1 = Matrix([1, 2, 3])
v2 = Matrix([4, 5, 5])

print(sqrt(sum([i**2 for i in v1])))
print(v1.dot(v2))   #скалярное произведение
print(v1.cross(v2))     #векторное произведение



