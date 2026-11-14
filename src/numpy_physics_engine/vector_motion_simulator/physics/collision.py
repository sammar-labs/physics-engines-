import numpy as np


def check_collision(particle_a, particle_b):
    difference = particle_a.position - particle_b.position
    distance = np.linalg.norm(difference)
    minimum_distance = particle_a.radius + particle_b.radius
    return distance <= minimum_distance
