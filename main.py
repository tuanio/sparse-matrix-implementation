from sparse_matrix import SparseMatrix

a = [[1, 0, 1, 2, 0, 4, 1],
    [2, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 2, 0, 0],
    [0, 3, 5, 2, 5, 1, 2]]

b = [[1, 0, 99, 2, 0, 4, 1],
    [100, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 3, 0, 2, 100, 1, 0]]

c = [[0, 2, 4, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 2, 3, 2],
    [0, 2, 0, 1],
    [0, 9, 0, 1]]

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