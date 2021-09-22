from typing import List, Dict


class SparseMatrix(object):
    def __init__(self, matrix, n: int = None, m: int = None):
        if type(matrix) == list:  # if matrix is list like
            self.dense_ = matrix
            self.n = len(matrix)
            self.m = len(matrix[0])
            self.sparse_ = self.__to_sparse()
        else:  # if matrix is a dictionary
            self.sparse_ = matrix
            self.n = n
            self.m = m

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

        A = self.sparse_
        B = obj.sparse_
        for i in range(self.n):
            for j in range(self.m):
                try:
                    A[(i, j)] = A[(i, j)] + B[(i, j)]
                except:
                    pass
        return SparseMatrix(A, self.n, self.m)

    def __sub__(self, obj: object):
        if self.n != obj.n or self.m != obj.m:
            raise Exception("Không cùng kích cỡ")

        A = self.sparse_
        B = obj.sparse_
        for i in range(self.n):
            for j in range(self.m):
                try:
                    A[(i, j)] = A[(i, j)] - B[(i, j)]
                except:
                    pass
        return SparseMatrix(A, self.n, self.m)

    def __mul__(self, obj: object):
        if self.n != obj.n or self.m != obj.m:
            raise Exception("Không cùng kích cỡ")

        A = self.sparse_
        B = obj.sparse_
        for i in range(self.n):
            for j in range(self.m):
                try:
                    A[(i, j)] = A[(i, j)] * B[(i, j)]
                except:
                    pass
        return SparseMatrix(A, self.n, self.m)

    def __matmul__(self, obj: object):
        if self.m != obj.n:
            raise Exception("Không cùng kích cỡ để nhân ma trận")

        A = self.sparse_
        B = obj.sparse_
        C = {}
        for i in range(self.n):
            for j in range(self.m):
                for k in range(obj.m):
                    try:
                        C[(i, k)] += A[(i, j)] * B[(j, k)]
                    except:
                        pass
        return SparseMatrix(C, self.n, obj.m)

    def transpose(self):
        A = {(j, i): val for (i, j), val in self.sparse_.items()}
        return SparseMatrix(A, self.m, self.n)

    def __repr__(self):
        return '<Sparse Matrix {0.n}x{0.m}>'.format(self)
