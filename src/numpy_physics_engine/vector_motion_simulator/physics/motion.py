import numpy as np
def calculate_velocity(displacement,delta_time):
    if delta_time<=0:
        raise ValueError("Time must be greater than zero")
    displacement=np.array(displacement,dtype=float)
    return displacement/delta_time

def final_velocity(u,a,t):
    return np.array(u,dtype=float)+np.array(a,dtype=float)*t

def displacement_from_acceleration(u,a,t):
    u=np.array(u,dtype=float)
    a=np.array(a,dtype=float)
    return u*t+0.5*a*t**2

if __name__=="__main__":
    print(calculate_velocity(100,300))