import numpy as np


def speed_to_color(velocity):
    velocity = np.array(velocity, dtype=float)
    speed = np.linalg.norm(velocity)
    intensity = np.clip(speed * 5, 0, 255)
    red = int(intensity)
    green = int(255 - intensity)
    blue = 255
    return np.array([red, green, blue], dtype=np.uint8)
