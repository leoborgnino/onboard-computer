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

imagen = "Images/trayectoria_rara.png"
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
path.smooth(0.5,0.35)
path_hard = path.path
path_soft = path.spath

print path_hard
print path_soft

## RUN Function

SCALE_FACTOR = 35 # Tile step
RAD_TO_DEG   = 180.0/math.pi
PHASE_LIMIT   = 5.0/RAD_TO_DEG
MODULE_LIMIT = 200.0/SCALE_FACTOR

vector_phase = 0.
vector_phase_old = 0.
vector_module = 0.
flag_alarm = 3

for i in range(len(path_soft)-1):
    vector = np.array( [path_soft[i+1][0] - path_soft[i][0],path_soft[i+1][1] - path_soft[i][1] ] )
    #print " Old : %f New: %f Result: %f " % (vector_phase,np.arctan(vector[1]/vector[0]),np.arctan(vector[1]/vector[0]) - vector_phase)
    vector_module = vector_module + np.sqrt(np.dot(vector, vector))
    vector_phase  = vector_phase + np.arctan(vector[1]/vector[0])
    print vector_module
    print vector_phase
    if (abs(vector_phase) > PHASE_LIMIT or vector_module > MODULE_LIMIT ):
        print " %f cm %f fase" % (vector_module*SCALE_FACTOR,vector_phase*RAD_TO_DEG)      
        datos = [chr(107)] + [chr(int(vector_module*SCALE_FACTOR))] + [chr(40)] + [chr(1)] + [chr(abs(int(vector_phase*RAD_TO_DEG)))] + [chr(0) if vector_phase*RAD_TO_DEG >= 0 else chr(1)]
        vector_module = 0.
        vector_phase = 0.
    if (flag_alarm == i):
        print "ERROR: Searching New Path"
        print "Point of error %d %d" % (path_soft[i+1][0],path_soft[i+1][1])
        error_path[0] = path_soft[i+1][0]
        error_path[1] = path_soft[i+1][1]
        new_init[0]   = path_soft[i][0]
        new_init[1]   = path_soft[i][1]
        break
    
if(self.flag_alarm):
    print "Generating new path. Error path: %d %d" % (error_path[0], error_path[1])
    self.path.grid[error_path[0]][error_path[1]] = 1
    self.path.init = new_init
    for i in range(len(self.path.grid)):
        print self.path.grid[i]
        print "Inicio: %d %d" % (self.path.init[0],self.path.init[1])
        print "Final:  %d %d" % (self.path.goal[0],self.path.goal[1])
        self.run()

x_hard = np.array(path_hard)[:,0]
y_hard = np.array(path_hard)[:,1]

x_soft = np.array(path_soft)[:,0]
y_soft = np.array(path_soft)[:,1]

plt.plot(x_hard,y_hard,'bo')
plt.plot(x_soft,y_soft,'r')
plt.grid(True)

plt.show()
