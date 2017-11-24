#from scipy import misc
from math import *
import random
import plan
import time
import numpy as np
#import matplotlib.pyplot as plt

m_plan       =           [[0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                          [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
                          [0, 0, 1, 0, 1, 0, 1, 0, 0, 0]]
init = [len(m_plan)-1,len(m_plan[0])-1]
goal = [0,0]

#imagen = "Images/imagenrgb0.jpg"
#m_imagen = misc.imread(imagen)
#m_plan = np.zeros((len(m_imagen),len(m_imagen[0])))
#for i in range(len(m_imagen)):
#    for j in range(len(m_imagen[0])):
#        if (m_imagen[i][j][0] > 200) and (m_imagen[i][j][1] > 200) and (m_imagen[i][j][2] > 200):
#            m_plan[i][j] = 0
#        elif (m_imagen[i][j][0] < 200) and (m_imagen[i][j][1] < 200) and (m_imagen[i][j][2] < 200):
#            m_plan[i][j] = 1
#        elif (m_imagen[i][j][0] > 200) and (m_imagen[i][j][1] < 100) and (m_imagen[i][j][2] < 100):
#            goal = [i,j]
#        elif (m_imagen[i][j][0] < 100) and (m_imagen[i][j][1] > 200) and (m_imagen[i][j][2] < 100):
#            init = [i,j]
for i in range(len(m_plan)):
    print m_plan[i]
print "Inicio: %d %d" % (init[0],init[1])
print "Final:  %d %d" % (goal[0],goal[1])
path = plan.plan(m_plan,init,goal)
path.astar()
path_hard = path.path
path_soft = path.smooth(path_hard)

print path_hard
print path_soft


