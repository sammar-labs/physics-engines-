import numpy as np


def rotational_matrix(angle_degrees):
    angle = np.radians(angle_degrees)
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])


def rotate_vector(vector, angle_degrees):
    vector = np.array(vector, dtype=float)
    matrix = rotational_matrix(angle_degrees)
    return matrix @ vector
