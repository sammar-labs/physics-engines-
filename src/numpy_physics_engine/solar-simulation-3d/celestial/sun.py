import math
from OpenGL.GL import *
from graphics.sphere import genrate_sphere
from config import SUN_RADIUS, SUN_COLOR, SPHERE_SEGMENTS, SPHERE_RINGS


class Sun:

  def __init__(self):
    self.vertices = genrate_sphere(SUN_RADIUS, SPHERE_SEGMENTS, SPHERE_RINGS)
    self.angle = 0.0

  def update(self, delta_time):
    self.angle += math.radians(10) * delta_time

  def draw(self):
    glPushMatrix()
    glRotatef(math.degrees(self.angle), 0, 1, 0)
    glColor3f(*SUN_COLOR)

    # glBegin loop ke BAHAR shuru hoga
    glBegin(GL_POINTS)
    for vertex in self.vertices:
      glVertex3f(vertex[0], vertex[1], vertex[2])
    # glEnd aur glPopMatrix loop ke BAHAR honge
    glEnd()

    glPopMatrix()