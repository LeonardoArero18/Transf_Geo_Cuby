from OpenGL.GL import *
import numpy as np

class CubeTransformations:
    def __init__(self):
        # Definindo os vértices e triângulos originais
        self.vertices = np.array([
            (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5),
            (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5),
            (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5), (0.5, 0.5, -0.5),
            (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)
        ], dtype=np.float32)
        
        self.triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
                        13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]
        
        self.original_vertices = self.vertices.copy()
    
    def reset(self):
        """Restaura os vértices originais"""
        self.vertices = self.original_vertices.copy()
    
    def translate(self, tx, ty, tz):
        """Aplica translação ao cubo"""
        translation = np.array([tx, ty, tz], dtype=np.float32)
        self.vertices += translation
    
    def scale(self, sx, sy, sz):
        """Aplica escala ao cubo"""
        scale_matrix = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, sz]], dtype=np.float32)
        self.vertices = np.dot(self.vertices, scale_matrix.T)
    
    def mirror(self, axis):
        """Aplica espelhamento em relação a um eixo ('x', 'y' ou 'z')"""
        if axis == 'x':
            mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32)
        elif axis == 'y':
            mirror_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]], dtype=np.float32)
        elif axis == 'z':
            mirror_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]], dtype=np.float32)
        else:
            raise ValueError("Eixo deve ser 'x', 'y' ou 'z'")
        
        self.vertices = np.dot(self.vertices, mirror_matrix.T)
    
    def rotate(self, angle_x, angle_y, angle_z):
        """Aplica rotação ao cubo (ângulos em graus)"""
        angle_x = np.radians(angle_x)
        angle_y = np.radians(angle_y)
        angle_z = np.radians(angle_z)
        
        # Matrizes de rotação
        rot_x = np.array([
            [1, 0, 0],
            [0, np.cos(angle_x), -np.sin(angle_x)],
            [0, np.sin(angle_x), np.cos(angle_x)]
        ], dtype=np.float32)
        
        rot_y = np.array([
            [np.cos(angle_y), 0, np.sin(angle_y)],
            [0, 1, 0],
            [-np.sin(angle_y), 0, np.cos(angle_y)]
        ], dtype=np.float32)
        
        rot_z = np.array([
            [np.cos(angle_z), -np.sin(angle_z), 0],
            [np.sin(angle_z), np.cos(angle_z), 0],
            [0, 0, 1]
        ], dtype=np.float32)
        
        # Combina as rotações
        rotation = rot_z @ rot_y @ rot_x
        self.vertices = np.dot(self.vertices, rotation.T)
    
    def draw_wire_cube(self):
        """Desenha o cubo em wireframe usando OpenGL"""
        for t in range(0, len(self.triangles), 3):
            glBegin(GL_LINE_LOOP)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t+1]])
            glVertex3fv(self.vertices[self.triangles[t+2]])
            glEnd()
