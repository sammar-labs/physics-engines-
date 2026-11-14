import numpy as np
def calculate_acceleration(initial_velocity,final_velocity,delta_time):
    if delta_time<=0:
        raise ValueError("EROORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    u =np.array(initial_velocity,dtype=float)
    v=np.array(final_velocity,dtype=float)
    return(v-u)/delta_time

if __name__=="__main__":
    print(calculate_acceleration(100,40,80))
        