import numpy as np


def create_matrix(values):
    return np.array(values, dtype=float)


def add_matrices(a, b):
    return np.add(a, b)


def multiply_matrices(a, b):
    return np.matmul(a, b)


def transpose_matrix(a):
    return np.transpose(a)


def determinant(a):
    return np.linalg.det(a)


def identity_matrix(size):
    return np.eye(size)
