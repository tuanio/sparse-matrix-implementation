from sparse_matrix import SparseMatrix
import numpy as np

n, m, k = 100, 100, 100

a = list(np.random.randint(0, 1000, size=(n, m)))
b = list(np.random.randint(0, 1000, size=(n, m)))
c = list(np.random.randint(0, 1000, size=(m, k)))

# a cùng kích cỡ với b
# a với c có thể nhân nghịch đảo

A = SparseMatrix(a)
B = SparseMatrix(b)
C = SparseMatrix(c)

add = A + B
sub = A - B
mul = A * B
mat_mul = A @ C
tranpose = A.transpose()

print(add, add.to_dense())
print(sub, sub.to_dense())
print(mul, mul.to_dense())
print(mat_mul, mat_mul.to_dense())
print(tranpose, tranpose.to_dense())