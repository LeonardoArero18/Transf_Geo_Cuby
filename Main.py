import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Cube import CubeTransformations

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    cube = CubeTransformations()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Teclas para controlar as transformações
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Rotação
                    cube.rotate(15, 15, 0)
                elif event.key == pygame.K_t:  # Translação
                    cube.translate(0.1, 0.1, 0)
                elif event.key == pygame.K_s:  # Escala
                    cube.scale(1.1, 1.1, 1.1)
                elif event.key == pygame.K_m:  # Espelhamento (eixo X)
                    cube.mirror('x')
                elif event.key == pygame.K_n:  # Reset
                    cube.reset()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube.draw_wire_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
