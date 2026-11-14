import numpy as np


class ParticleManager:
    def __init__(self):
        self.particles = []

    def add(self, particle):
        self.particles.append(particle)

    def remove(self, index):
        self.particles.pop(index)

    def get_positions(self):
        if not self.particles:
            return np.empty((0, 2), dtype=float)
        return np.array([particle.position for particle in self.particles])

    def count(self):
        return len(self.particles)
