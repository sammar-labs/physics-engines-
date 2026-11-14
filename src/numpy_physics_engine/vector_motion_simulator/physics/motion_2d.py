import numpy as np
def update_position(position,velocity,acceleration,dt):
    position=np.array(position,dtype=float)
    velocity=np.array(velocity,dtype=float)
    acceleration=np.array(acceleration,dtype=float)
    new_position=(
        position+velocity*dt+0.5*acceleration*dt**2
                  )
    new_velocity=velocity+acceleration*dt
    return new_position,new_velocity