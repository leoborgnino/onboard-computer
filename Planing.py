from scipy import misc
from math import *
import random
from Obj_Head import Obj_Head
import plan
import time
import math
import numpy as np
import matplotlib.pyplot as plt

MODE_SIM      = 0
SCALE_FACTOR  = 26 # Tile step
RAD_TO_DEG    = 180.0/math.pi
MODE_ACCUM    = 1
PHASE_LIMIT   = 10.0/RAD_TO_DEG
MODULE_LIMIT  = 200.0/SCALE_FACTOR
VELOCIDAD     = 45

class Planing(Obj_Head):

    def __init__(self,com,imagen):
        self.commands_file = open('commands.log','w')
        self.iterations    = 0
        self.flag_iteration = 1
        self.all_paths_x    = []
        self.all_paths_y    = []
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
        path_index = [0]
        stop       = False
        while (self.flag_iteration and (stop == False) ):
            error_path = [0,0]
            new_init   = [0,0]
            stop = self.path.astar()
            if (self.flag_iteration == 0):
                self.path.smooth(0.5,0.35)
            self.flag_iteration = 0
            if ( stop == False ) :
                path_hard = self.path.path
                path_soft = self.path.spath
                vector_phase = 0.
                vector_module = 0.
                i = 0
                while (i < (len(path_soft)-1)):
                    vector = np.array( [path_soft[i+1][0] - path_soft[i][0],path_soft[i+1][1] - path_soft[i][1] ] )
                    #print " Old : %f New: %f Result: %f " % (vector_phase,np.arctan(vector[1]/vector[0]),np.arctan(vector[1]/vector[0]) - vector_phase)
                    vector_module = vector_module + np.sqrt(np.dot(vector, vector))
                    delta_phase = abs(vector_phase_old - np.arctan(vector[1]/vector[0]))
                    vector_phase  = vector_phase + np.arctan(vector[1]/vector[0])
                    if ( (delta_phase > PHASE_LIMIT  or vector_module > MODULE_LIMIT or (i == len(path_soft)-2)) or (not MODE_ACCUM) ):
                        datos = [chr(107)] + [chr(int(vector_module*SCALE_FACTOR)&0xFF)] + [chr((int(vector_module*SCALE_FACTOR)&0xFF00)>>8)] + [chr(VELOCIDAD)] + [chr(1)] + [chr(abs(int(vector_phase*RAD_TO_DEG)))] + [chr(0) if vector_phase*RAD_TO_DEG >= 0 else chr(1)]
                        print "Avanzar %f centimetros a %f grados" % (vector_module*SCALE_FACTOR,vector_phase*RAD_TO_DEG)      
                        self.commands_file.write("Avanzar %f centimetros a %f grados\n" % (vector_module*SCALE_FACTOR,vector_phase*RAD_TO_DEG))      
                        self.send(datos)
                        vector_phase_old = vector_phase
                        vector_module = 0.
                        vector_phase = 0.
                        while not self.__flag :
                            pass
                        if ( self.flag_alarm and not (i == len(path_soft)-2)):
                            print "ERROR: Searching New Path"
                            print "Point of error %d %d" % (path_hard[i+1][0],path_hard[i+1][1])
                            error_path[0] = path_hard[i+1][0]
                            error_path[1] = path_hard[i+1][1]
                            new_init[0]   = path_hard[i][0]
                            new_init[1]   = path_hard[i][1]
                            break
                        else:
                            i += 1
                        self.__flag = 0
                    else:
                        i += 1
                if( self.flag_alarm ):
                    print "Generating new path. Error path: %d %d" % (error_path[0], error_path[1])
                    if (vector_phase_old >= 45 and vector_phase_old < 135):
                        self.path.grid[error_path[0]][error_path[1]] = 1
                        self.path.grid[error_path[0]][error_path[1]-1] = 1
                        self.path.grid[error_path[0]][error_path[1]+1] = 1
                        self.path.grid[error_path[0]-1][error_path[1]] = 1
                        self.path.grid[error_path[0]-1][error_path[1]-1] = 1
                        self.path.grid[error_path[0]-1][error_path[1]+1] = 1
                    elif (vector_phase_old < 45 and vector_phase_old > -45):
                        self.path.grid[error_path[0]][error_path[1]] = 1
                        self.path.grid[error_path[0]-1][error_path[1]] = 1
                        self.path.grid[error_path[0]+1][error_path[1]] = 1
                        self.path.grid[error_path[0]][error_path[1]-1] = 1
                        self.path.grid[error_path[0]-1][error_path[1]-1] = 1
                        self.path.grid[error_path[0]+1][error_path[1]-1] = 1
                    elif (vector_phase_old >= 135 or vector_phase_old <= -135):
                        self.path.grid[error_path[0]][error_path[1]] = 1
                        self.path.grid[error_path[0]][error_path[1]-1] = 1
                        self.path.grid[error_path[0]][error_path[1]+1] = 1
                        self.path.grid[error_path[0]+1][error_path[1]] = 1
                        self.path.grid[error_path[0]+1][error_path[1]-1] = 1
                        self.path.grid[error_path[0]+1][error_path[1]+1] = 1
                    elif (vector_phase_old <= -45 and vector_phase_old > -135):
                        self.path.grid[error_path[0]][error_path[1]] = 1
                        self.path.grid[error_path[0]][error_path[1]-1] = 1
                        self.path.grid[error_path[0]][error_path[1]+1] = 1
                        self.path.grid[error_path[0]+1][error_path[1]] = 1
                        self.path.grid[error_path[0]+1][error_path[1]-1] = 1
                        self.path.grid[error_path[0]+1][error_path[1]+1] = 1
                    self.path.init = new_init
                    for j in range(len(self.path.grid)):
                        print self.path.grid[j]
                    print "Inicio: %d %d" % (self.path.init[0],self.path.init[1])
                    print "Final:  %d %d" % (self.path.goal[0],self.path.goal[1])
                    self.flag_alarm = 0
                    self.__flag = 0
                    self.all_paths_x.append(np.array(path_soft)[:,0])
                    self.all_paths_y.append(np.array(path_soft)[:,1])
                    path_index.append(i)
                    self.flag_iteration = 1

        self.all_paths_x.append(np.array(path_soft)[:,0])
        self.all_paths_y.append(np.array(path_soft)[:,1])
        print len(self.all_paths_x)
        print self.all_paths_x
        print path_index
        x_soft = self.all_paths_x[0]
        y_soft = self.all_paths_y[0]
        plt.plot(x_soft,y_soft,'bo-')
        path_iter = 0
        for j in range(1,len(self.all_paths_x)):
            path_iter = path_iter + path_index[j]
            print path_iter
            print self.all_paths_x[j]
            for k in range(path_iter):
                self.all_paths_x[j] = np.insert(self.all_paths_x[j],k,self.all_paths_x[j-1][k])
                self.all_paths_y[j] = np.insert(self.all_paths_y[j],k,self.all_paths_y[j-1][k])
            print self.all_paths_x[j]
            x_soft = self.all_paths_x[j]
            y_soft = self.all_paths_y[j]
            plt.plot(x_soft,y_soft)
        x_grid = []
        y_grid = []
        for i in range(len(self.path.grid)):
            for j in range(len(self.path.grid[0])):
                if (self.path.grid[i][j] == 1):
                    y_grid.append(j)
                    x_grid.append(i)
        plt.plot(x_grid,y_grid,'ro')
        plt.show()

    def flag(self,datos):
                #print "Dato answ: %d "%datos[0]
                self.flag_alarm = True if datos[0] == 49 else False
                self.__flag = 1
                print "FLAG: %d"%self.flag_alarm
