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

        draw_triangle()
        draw_circle()
        draw_square()

        pygame.display.flip()
        pygame.time.wait(10)

def draw_triangle():
    # Desenha o triângulo
    glBegin(GL_TRIANGLES)
    glVertex3f(-3, 1, 0)    # Ponto inferior esquerdo
    glVertex3f(-1, 1, 0)    # Ponto inferior direito
    glVertex3f(-2, 2, 0)    # Ponto superior
    glEnd()

    # Desenha o triângulo refletido
    glBegin(GL_TRIANGLES)
    glVertex3f(-3, -1, 0)    # Ponto inferior esquerdo
    glVertex3f(-1, -1, 0)    # Ponto inferior direito
    glVertex3f(-2, -2, 0)    # Ponto superior
    glEnd()

def draw_circle():
    # Desenha a circunferência
    x_circle = 6
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


    # Desenha a circunferência refletida
    x_circle = -6
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

def draw_square():
    # Desenha o quadrado
    vertices = (
        (4, 3, 0),
        (4, 2, 0),
        (3, 2, 0),
        (3, 3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

    # Desenha o quadrado refletido
    ## Reflexao eixo X
    vertices = (
        (4, -3, 0),
        (4, -2, 0),
        (3, -2, 0),
        (3, -3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

    ## Reflexao eixo Y
    vertices = (
        (-4, 3, 0),
        (-4, 2, 0),
        (-3, 2, 0),
        (-3, 3, 0))

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

if __name__ == '__main__':
    draw()