import numpy as np
class particle:
    def __init__(self,x,y,radius,color):
        
        self.color=np.array(color,
                            dtype=np.uint8)
        self.position=np.array([x,y],dtype=np.float64)
        self.radius=int(radius)

if __name__=="__main__":
    particles=particle(12,5,90,3)
    print(particles.radius)
        