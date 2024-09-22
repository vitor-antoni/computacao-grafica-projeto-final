import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    gluPerspective(75, (display[0]/display[1]), 0.1, 80.0)
    glTranslatef(0.0,0.0, -5)
    
    # Define cor azul
    glColor3f(0,0,1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        draw_point(2, 3, 20)

        pygame.display.flip()
        pygame.time.wait(10)

def draw_point(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    

if __name__ == "__main__":
    draw()



