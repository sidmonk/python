import numpy as np

m = np.array([[2, 3], [5, 6]])

a = np.linalg.matrix_power(m, 2)

print(np.dot(np.linalg.inv(m), m))