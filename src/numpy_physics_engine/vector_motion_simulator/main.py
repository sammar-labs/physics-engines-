import os
import numpy as np
from particle.particle import particle
from particle.particle_manager import ParticleManager
from graphics.canvas import canvas
from graphics.renderer import Render
from graphics.ppm_writer import save_ppm
from mathematics.coordinates import coordinates
from physics.motion_2d import update_position
from physics.gravity import gravity_acceleration
from physics.time_engine import TimeEngine
from graphics.video_writer import create_video
WIDTH=800
HEIGHT=600
TOTAL_FRAMES=75
os.makedirs("output/frames",exist_ok=True)
canvas=canvas(WIDTH,HEIGHT)
renderer=Render()
coordinates=coordinates(WIDTH,HEIGHT)
clock=TimeEngine(0.1)
manager=ParticleManager()
particle=particle(x=0,y=100,radius=10,color=[0,150,255])
manager.add(particle)
velocity=np.array([20.0,10.0])
acceleration=gravity_acceleration()
for frame in range(TOTAL_FRAMES):
    new_position,new_velocity=update_position(particle.position,velocity,acceleration,clock.delta_time)
    particle.position=new_position
    velocity=new_velocity
    canvas.clear()
    for current_particle in manager.particles:
        renderer.draw_particle(
            canvas,
            current_particle,
            coordinates
        )
        filename=f"output/frames/frame_{frame:03d}.ppm"
        save_ppm(canvas.pixels,filename)
        clock.update()
        print("Frame",frame,"Position:",particle.position)
        
create_video(frames_directory="output/frames",
             output_file="output/physics_simulation.mp4",
             fps=30)
