#!/usr/bin/python

import pygame
import urllib
from OpenGL.GL import *
from OpenGL.GLU import *
from math import radians
from pygame.locals import *
import pruebaserver


class grafico:

    SCREEN_SIZE = (800, 600)
    SCALAR2 = 0.2
    SCALAR = .5

    def __init__(self,acelerometro):
	#server = pruebaserver.index()
	self.acelerometro = acelerometro

    def resize(self,width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / height, 0.001, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0.0, 1.0, -5.0,
                  0.0, 0.0, 0.0,
                  0.0, 1.0, 0.0)
        
    def init(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_BLEND)
        glEnable(GL_POLYGON_SMOOTH)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1.0));
    
    def read_values(self):
        #link = "http://192.168.0.31:8080" # Change this address to your settings
        #f = urllib.urlopen(link)
        #myfile = f.read()
        #return myfile.split(" ")
        self.acelerometro.obtener_datos()
        return [self.acelerometro.x_rotation, self.acelerometro.y_rotation]

    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.SCREEN_SIZE, HWSURFACE | OPENGL | DOUBLEBUF)
        self.resize(*self.SCREEN_SIZE)
        self.init()
        clock = pygame.time.Clock()
        cube = Cube((0.0, 0.0, 0.0), (.5, .5, .7))
        angle = 0
        
        while True:
            then = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == KEYUP and event.key == K_ESCAPE:
                    return
    
            values = self.read_values()
            #print values
            x_angle = values[0]
            y_angle = values[1]
    
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
            glColor((1.,1.,1.))
            glLineWidth(1)
            glBegin(GL_LINES)
    
            for x in range(-20, 22, 2):
                glVertex3f(x/10.,-1,-1)
                glVertex3f(x/10.,-1,1)
            
            for x in range(-20, 22, 2):
                glVertex3f(x/10.,-1, 1)
                glVertex3f(x/10., 1, 1)
            
            for z in range(-10, 12, 2):
                glVertex3f(-2, -1, z/10.)
                glVertex3f( 2, -1, z/10.)
    
            for z in range(-10, 12, 2):
                glVertex3f(-2, -1, z/10.)
                glVertex3f(-2,  1, z/10.)
    
            for z in range(-10, 12, 2):
                glVertex3f( 2, -1, z/10.)
                glVertex3f( 2,  1, z/10.)
    
            for y in range(-10, 12, 2):
                glVertex3f(-2, y/10., 1)
                glVertex3f( 2, y/10., 1)
            
            for y in range(-10, 12, 2):
                glVertex3f(-2, y/10., 1)
                glVertex3f(-2, y/10., -1)
            
            for y in range(-10, 12, 2):
                glVertex3f(2, y/10., 1)
                glVertex3f(2, y/10., -1)
            
            glEnd()
            glPushMatrix()
            glRotate(float(x_angle), 1, 0, 0)
            glRotate(-float(y_angle), 0, 0, 1)
            cube.render()
            glPopMatrix()
            pygame.display.flip()
    
class Cube(object):

    def __init__(self, position, color):
        self.position = position
        self.color = color

    # Cube information
    num_faces = 6

    vertices = [ (-1.0, -0.05, 0.5),
                 (1.0, -0.05, 0.5),
                 (1.0, 0.05, 0.5),
                 (-1.0, 0.05, 0.5),
                 (-1.0, -0.05, -0.5),
                 (1.0, -0.05, -0.5),
                 (1.0, 0.05, -0.5),
                 (-1.0, 0.05, -0.5) ]

    normals = [ (0.0, 0.0, +1.0),  # front
                (0.0, 0.0, -1.0),  # back
                (+1.0, 0.0, 0.0),  # right
                (-1.0, 0.0, 0.0),  # left
                (0.0, +1.0, 0.0),  # top
                (0.0, -1.0, 0.0) ]  # bottom

    vertex_indices = [ (0, 1, 2, 3),  # front
                       (4, 5, 6, 7),  # back
                       (1, 5, 6, 2),  # right
                       (0, 4, 7, 3),  # left
                       (3, 2, 6, 7),  # top
                       (0, 1, 5, 4) ]  # bottom

    def render(self):
        then = pygame.time.get_ticks()
        glColor(self.color)

        vertices = self.vertices

        # Draw all 6 faces of the cube
        glBegin(GL_QUADS)

        for face_no in xrange(self.num_faces):
            glNormal3dv(self.normals[face_no])
            v1, v2, v3, v4 = self.vertex_indices[face_no]
            glVertex(vertices[v1])
            glVertex(vertices[v2])
            glVertex(vertices[v3])
            glVertex(vertices[v4])
        glEnd()

