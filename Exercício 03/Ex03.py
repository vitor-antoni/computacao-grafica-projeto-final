import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

triangle_pos_x = 0.0
triangle_pos_y = 0.0
triangle_scale = 1.0
triangle_rotation = 0.0

def draw():
    global triangle_pos_x, triangle_pos_y, triangle_scale, triangle_rotation

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    gluPerspective(110, (display[0]/display[1]), 0.1, 110.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # Mover o triângulo com as setas do teclado
        if keys[pygame.K_LEFT]:
            triangle_pos_x -= 0.05

        elif keys[pygame.K_RIGHT]:
            triangle_pos_x += 0.05

        elif keys[pygame.K_UP]:
            triangle_pos_y += 0.05

        elif keys[pygame.K_DOWN]:
            triangle_pos_y -= 0.05

        # Aumentar o tamanho do triângulo (tecla A)
        if keys[pygame.K_a]:
            triangle_scale += 0.01

        # Diminuir o tamanho do triângulo (tecla D)
        elif keys[pygame.K_d]:
            triangle_scale -= 0.01

            if triangle_scale < 0.1:
                triangle_scale = 0.1

        # Rotacionar o triângulo em sentido horário (tecla Q)
        if keys[pygame.K_q]:
            triangle_rotation += 90

        # Rotacionar o triângulo em sentido anti-horário (tecla E)
        elif keys[pygame.K_e]:
            triangle_rotation -= 90

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        glPushMatrix()
        glTranslatef(triangle_pos_x, triangle_pos_y, 0)
        glRotatef(triangle_rotation, 0, 0, 1)
        glScalef(triangle_scale, triangle_scale, 1.0)

        draw_triangle()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex3f(-3, 1, 0)    # Ponto inferior esquerdo
    glVertex3f(-1, 1, 0)    # Ponto inferior direito
    glVertex3f(-2, 2, 0)    # Ponto superior
    glEnd()


if __name__ == '__main__':
    draw()
