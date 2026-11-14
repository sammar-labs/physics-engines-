import numpy as np
GRAVITY=9.8
def gravity_acceleration():
    return np.array([0.0,-GRAVITY])
def gravitational_force(mass):
    return mass*GRAVITY

if __name__=="__main__":
    gravitational_force(100)
    gravity_acceleration()