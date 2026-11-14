import numpy as np
class canvas:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.pixels=np.zeros((height,width,3),
                             dtype=np.uint8)
    def clear(self):
        self.pixels.fill(0)


if __name__=="__main__":
    canva=canvas(800,700)

    print(canva.pixels.shape)
            
    