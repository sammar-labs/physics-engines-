import numpy as np
def uniform_position(initial_position,velocity,time):
    r0=np.array(initial_position,dtype=float)
    v=np.array(velocity,dtype=float)
    return r0+v*time

if __name__=="__main__":
    print(uniform_position(12,3,90))