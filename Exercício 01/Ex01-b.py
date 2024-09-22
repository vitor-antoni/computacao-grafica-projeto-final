import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    x1 = int(input("Valor de X1: "))
    y1 = int(input("Valor de Y1: "))
    x2 = int(input("Valor de X2: "))
    y2 = int(input("Valor de Y2: "))
    
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

        draw_line(x1, y1, x2, y2)

        pygame.display.flip()
        pygame.time.wait(10)

def draw_line(X1, Y1, X2, Y2):
    glBegin(GL_LINES)
    glVertex2i(X1, Y1)
    glVertex2i(X2, Y2)
    glEnd()


if __name__ == "__main__":
    draw()