from scipy import misc
from math import *
import random
from Obj_Head import Obj_Head
import plan
import time
import numpy as np

class Planing(Obj_Head):

    def __init__(self,com,imagen):
        
        ''''self.grid       =           [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                             [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                                         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                                         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                                         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        
        '''
        self.m_imagen = misc.imread(imagen)
        self.m_plan = np.zeros((len(self.m_imagen),len(self.m_imagen[0])))
        for i in range(len(self.m_imagen)):
            for j in range(len(self.m_imagen[0])):
                if (self.m_imagen[i][j][0] > 200) and (self.m_imagen[i][j][1] > 200) and (self.m_imagen[i][j][2] > 200):
                    self.m_plan[i][j] = 0
                elif (self.m_imagen[i][j][0] < 200) and (self.m_imagen[i][j][1] < 200) and (self.m_imagen[i][j][2] < 200):
                    self.m_plan[i][j] = 1
                elif (self.m_imagen[i][j][0] > 200) and (self.m_imagen[i][j][1] < 100) and (self.m_imagen[i][j][2] < 100):
                    self.goal = [i,j]
                elif (self.m_imagen[i][j][0] < 100) and (self.m_imagen[i][j][1] > 200) and (self.m_imagen[i][j][2] < 100):
                    self.init = [i,j]
        for i in range(len(self.m_plan)):
            print self.m_plan[i]
        print "Inicio: %d %d" % (self.init[0],self.init[1])
        print "Final:  %d %d" % (self.goal[0],self.goal[1])
        self.tita = 0
        self.contador = 0
        Obj_Head.__init__(self,com,self.flag)
        self.path = plan.plan(self.m_plan,self.init,self.goal)
        self.__flag = 0
                self.flag_alarm = False;
    
    def run(self):
                error_path = [0,0]
                new_init   = [0,0]
        contador = 1
        self.path.astar()
        for i  in range(len(self.path.path) - 1):
            self.paso = self.path.action[self.path.path[i+1][0]][self.path.path[i+1][1]]
            self.rotacion = (self.paso - self.tita) * 90
            if self.rotacion > 180:
                self.rotacion = self.rotacion - 360
            if self.rotacion < -180:
                self.rotacion = self.rotacion + 360

            if self.rotacion != 0:
                datos = [chr(102)] + [chr(abs(self.rotacion))] + [chr(1) if self.rotacion > 0 else chr(0)] 
                self.send(datos)
                while not self.__flag:
                    pass
                self.__flag = 0
                datos = [chr(100)] + [chr(60)] + [chr(40)] + [chr(0)]
                #contador = 0
                self.send(datos)
                while not self.__flag:
                    pass
                                print("%s.Rotar %s grados" % (i,self.rotacion))
                                if (self.flag_alarm):
                                        print "ERROR: Searching New Path"
                                        print "Point of error %d %d" % (self.path.path[i+1][0],self.path.path[i+1][1])
                self.__flag = 0
            else:
                datos = [chr(100)] + [chr(60)] + [chr(40)] + [chr(0)]
                #contador = 0
                self.send(datos)
                while not self.__flag:
                    pass
                                if (self.flag_alarm):
                                        print "ERROR: Searching New Path"
                                        print "Point of error %d %d" % (self.path.path[i+1][0],self.path.path[i+1][1])
                                        error_path[0] = self.path.path[i+1][0]
                                        error_path[1] = self.path.path[i+1][1]
                                        new_init[0]   = self.path.path[i][0]
                                        new_init[1]   = self.path.path[i][1]
                                        break
                self.__flag = 0
            self.__flag = 0
            print 'Adelante 30 cm'
        
            self.tita = self.tita + (self.paso-self.tita)
            if self.tita > 4:
                self.tita = 0
            if self.tita < -1:
                self.tita = 3
                if(self.flag_alarm):
                        print "Generating new path. Error path: %d %d" % (error_path[0], error_path[1])
                        self.path.grid[error_path[0]][error_path[1]] = 1
                        self.path.init = new_init
                        for i in range(len(self.path.grid)):
                                print self.path.grid[i]
                        print "Inicio: %d %d" % (self.path.init[0],self.path.init[1])
                        print "Final:  %d %d" % (self.path.goal[0],self.path.goal[1])
            self.run()
    def flag(self,datos):
                self.flag_alarm = True if datos[0] == 49 else False
                self.__flag = 1
