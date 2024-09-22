import pygame
import math
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    gluPerspective(110, (display[0]/display[1]), 0.1, 110.0)
    glTranslatef(0.0,0.0, -5)
    
    # Define cor azul
    glColor3f(0,0,1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        draw_body()
        draw_head()
        draw_legs()
        draw_arms()

        pygame.display.flip()
        pygame.time.wait(10)

def draw_body():
    glBegin(GL_TRIANGLES)
    glVertex3f(-1, 1, 0)    # Ponto inferior esquerdo
    glVertex3f(1, 1, 0)     # Ponto inferior direito
    glVertex3f(0, 3, 0)     # Ponto superior
    glEnd()

def draw_head():
    x_circle = 0
    y_circle = 4
    
    raio = 1
    segmento = 360

    glBegin(GL_TRIANGLE_FAN)
    for i in range(segmento):
        angle = 2 * math.pi * i / segmento
        x = raio * math.cos(angle)
        y = raio * math.sin(angle)
        glVertex3f(x + x_circle, y + y_circle, 0)
    glEnd()

def draw_legs():
    # Perna direita
    vertices = (
        (0.4, 1, 0),
        (0.4, 0, 0),
        (0.2, 0, 0),
        (0.2, 1, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

    # Perna esquerda
    vertices = (
        (-0.4, 1, 0),
        (-0.4, 0, 0),
        (-0.2, 0, 0),
        (-0.2, 1, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def draw_arms():
    # Braço direito
    glBegin(GL_LINES)
    glVertex2i(0, 2)
    glVertex2i(2, 2)
    glEnd()

    # Braço esquerdo
    glBegin(GL_LINES)
    glVertex2i(0, 2)
    glVertex2i(-2, 2)
    glEnd()

if __name__ == '__main__':
    draw()