from scipy import misc
import math 
import random
import plan
import time
import numpy as np
import matplotlib.pyplot as plt

#m_plan       =           [[0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
#                          [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
#                          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#                          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#                          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#                          [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
#                          [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
#                          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#                          [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
#                          [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
#                          [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
#                          [0, 0, 1, 0, 1, 0, 1, 0, 0, 0]]
#init = [len(m_plan)-1,len(m_plan[0])-1]
#goal = [0,0]

imagen = "Images/imagenrgb1.jpg"
m_imagen = misc.imread(imagen)
m_plan = np.zeros((len(m_imagen),len(m_imagen[0])))
for i in range(len(m_imagen)):
    for j in range(len(m_imagen[0])):
        if (m_imagen[i][j][0] > 200) and (m_imagen[i][j][1] > 200) and (m_imagen[i][j][2] > 200):
            m_plan[i][j] = 0
        elif (m_imagen[i][j][0] < 200) and (m_imagen[i][j][1] < 200) and (m_imagen[i][j][2] < 200):
            m_plan[i][j] = 1
        elif (m_imagen[i][j][0] > 200) and (m_imagen[i][j][1] < 100) and (m_imagen[i][j][2] < 100):
            goal = [i,j]
        elif (m_imagen[i][j][0] < 100) and (m_imagen[i][j][1] > 200) and (m_imagen[i][j][2] < 100):
            init = [i,j]

for i in range(len(m_plan)):
    print m_plan[i]
print "Inicio: %d %d" % (init[0],init[1])
print "Final:  %d %d" % (goal[0],goal[1])
path = plan.plan(m_plan,init,goal)
path.astar()
path.smooth(0.5,0.25)
path_hard = path.path
path_soft = path.spath

print path_hard
print path_soft

## RUN Function

SCALE_FACTOR = 30 # Tile step
RAD_TO_DEG   = 180.0/math.pi

vector_phase = 0.
vector_phase_old = 0.
for i in range(len(path_soft)-1):
    vector = np.array( [path_soft[i+1][0] - path_soft[i][0],path_soft[i+1][1] - path_soft[i][1] ] )
    #print " Old : %f New: %f Result: %f " % (vector_phase,np.arctan(vector[1]/vector[0]),np.arctan(vector[1]/vector[0]) - vector_phase)
    vector_module = np.sqrt(np.dot(vector, vector))
    vector_phase  =  np.arctan(vector[1]/vector[0]) - vector_phase_old
    vector_phase_old = np.arctan(vector[1]/vector[0])
    
    print "Avanzar %f centimetros a %f grados" % (vector_module*SCALE_FACTOR,vector_phase*RAD_TO_DEG)



x_hard = np.array(path_hard)[:,0]
y_hard = np.array(path_hard)[:,1]

x_soft = np.array(path_soft)[:,0]
y_soft = np.array(path_soft)[:,1]

plt.plot(x_hard,y_hard,'bo')
plt.plot(x_soft,y_soft,'r')
plt.grid(True)

plt.show()
