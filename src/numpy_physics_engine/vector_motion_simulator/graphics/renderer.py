import numpy as np
class Render:
    def draw_particle(self,canvas,particle,coordinates):
        center_x,center_y=coordinates.to_pixel(
            particle.position
            )
        y,x=np.ogrid[
            :canvas.height,
                    :canvas.width
                     ]
        mask=((x-center_x)**2+(y-center_y)**2)<=particle.radius**2
        canvas.pixels[mask]=particle.color

if __name__=="__main__":
    render=Render()