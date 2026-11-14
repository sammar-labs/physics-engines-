import numpy as np
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import (
    glClear,
    glClearColor,
    glEnable,
    glViewport,
    glMatrixMode,
    glLoadIdentity,
    glTranslatef,
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
    GL_DEPTH_TEST,
    GL_PROJECTION,
    GL_MODELVIEW,
)
from OpenGL.GLU import gluPerspective
from celestial.sun import Sun


def main():
    pygame.init()
    width = 1000
    height = 700
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("SolarSim3D")

    glViewport(0, 0, width, height)
    glClearColor(0.02, 0.02, 0.08, 1.0)
    glEnable(GL_DEPTH_TEST)

    # 3D Camera Perspective set karna
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 1000.0)

    glMatrixMode(GL_MODELVIEW)

    sun = Sun()
    clock = pygame.time.Clock()
    running = True

    while running:
        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Sun ko update karna
        sun.update(delta_time)

        # Screen saaf karna aur camera ko peeche rakhna taake Sun nazar aaye
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -15.0)  # Camera ko 15 units peeche kiya

        # Sun ko screen par draw karna
        sun.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
