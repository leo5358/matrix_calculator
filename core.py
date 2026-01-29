import numpy as np

class MatrixLogic:
    @staticmethod
    def parse_matrix_text(text):
        """將字串輸入解析為 Numpy Array"""
        try:
            matrix = []
            for line in text.strip().split("\n"):
                if line.strip(): 
                    matrix.append([float(x) for x in line.split()])
            if not matrix:
                return None
            return np.array(matrix)
        except ValueError:
            raise ValueError("Invalid numbers")

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a @ b

    @staticmethod
    def transpose(a):
        return a.T

    @staticmethod
    def determinant(a):
        if a.shape[0] != a.shape[1]:
            raise ValueError("Matrix must be square")
        return np.linalg.det(a)

    @staticmethod
    def inverse(a):
        if a.shape[0] != a.shape[1]:
            raise ValueError("Matrix must be square")
        return np.linalg.inv(a)

    @staticmethod
    def scalar_multiply(a, scalar_val):
        return a * scalar_val

    @staticmethod
    def identity(size):
        return np.eye(size)