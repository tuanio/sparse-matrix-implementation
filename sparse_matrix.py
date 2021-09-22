from typing import List, Dict


class SparseMatrix(object):
    def __init__(self, matrix: List[List]):
        self.dense_ = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.sparse_ = self.__to_sparse()

    def __to_sparse(self) -> Dict:
        sparse_matrix = {}
        for i in range(self.n):
            for j in range(self.m):
                if self.dense_[i][j]:
                    sparse_matrix[(i, j)] = self.dense_[i][j]
        return sparse_matrix

    def to_dense(self) -> List[List]:
        dense_matrix = [[0 for i in range(self.m)] for j in range(self.n)]
        for (i, j), val in self.sparse_.items():
            dense_matrix[i][j] = val
        return dense_matrix

    def __add__(self, obj: object):
        if self.n != obj.n or self.m != obj.m:
            raise Exception("Không cùng kích cỡ")

        A = self.to_dense()
        B = obj.to_dense()
        for i in range(self.n):
            for j in range(self.m):
                A[i][j] += B[i][j]
        return SparseMatrix(A)

    def __sub__(self, obj: object):
        if self.n != obj.n or self.m != obj.m:
            raise Exception("Không cùng kích cỡ")

        A = self.to_dense()
        B = obj.to_dense()
        for i in range(self.n):
            for j in range(self.m):
                A[i][j] -= B[i][j]
        return SparseMatrix(A)

    def __mul__(self, obj: object):
        if self.n != obj.n or self.m != obj.m:
            raise Exception("Không cùng kích cỡ")

        A = self.to_dense()
        B = obj.to_dense()
        for i in range(self.n):
            for j in range(self.m):
                A[i][j] *= B[i][j]
        return SparseMatrix(A)

    def __matmul__(self, obj: object):
        if self.m != obj.n:
            raise Exception("Không cùng kích cỡ để nhân ma trận")

        A = self.to_dense()
        B = obj.to_dense()
        C = [[0 for i in range(obj.m)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                for k in range(obj.m):
                    C[i][k] += A[i][j] * B[j][k]
        return SparseMatrix(C)

    def transpose(self):
        A = self.to_dense()
        B = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                B[j][i] = A[i][j]
        return SparseMatrix(B)

    def __repr__(self):
        return '<Sparse Matrix {0.n}x{0.m}>'.format(self)
