import numpy as np
import math as m
from CoordinatesTransform import *
from DesiredTrajectory import *
from Dynamics import *

""" Instance """

coordTrans = TransCoord()
DesTrj = DesiredTrajectory()
Dyn = Dynamics()


""" Variables """ 

simulationTime = 30
samplingTime = 0.01

R2D = 180 / m.pi
D2R = m.pi / 180

gravityAcc = 9.81
vectorG = [0, 0, gravityAcc]    # Gravity Acceleration Vector (NED - North East Down)
rho = 1024.8103                 # sea water density (temp 20 deg celcius : ref. ITTC Water properties 

# Unit Matrix
unitI = [1, 0, 0]
unitJ = [0, 1, 0]
unitK = [0, 0, 1]
unitZ = [0, 0, 0, 1]

#HAUV Initial Velue
hauvInitPos = [[-2, -2, 0], [10, 10, 30] * D2R]
hauvInitVel = [[0, 0, 0], [0, 0, 0] * D2R]


""" Parameters for making trajectory """
# Time section according to desired position and orientation
timeSection = [ [0, 10, 20, 30], 
                [0, 10, 20, 30], 
                [0, 10, 20, 30], 
                [0, 10, 20, 30], 
                [0, 10, 20, 30], 
                [0, 10, 20, 30] ] 

# Des Position and Orientation
targetPos = []
targetPos[:, 1] = [ [0, 0, 0], [0, 0, 0] * D2R ]
targetPos[:, 2] = [ [8, -10, 5], [0, 0, -30] * D2R ]
targetPos[:, 3] = [ [15, -3, 10], [0, 0, -90] * D2R ];
targetPos[:, 4] = [ [10, 5, 15], [0, 0, 0] * D2R ];

vectorTGT = []

for i in range(4 - 1):      # 4 is number of second dimension in targetPos 
    for j in range(6):
        matTRJ  =  [[timeSection[j][i]**3, timeSection[j][i]**2, timeSection[j][i], 1],
                    [timeSection[j][i + 1]**3, timeSection[j][i + 1]**2, timeSection[j][i + 1], 1],
                    [3 * timeSection[j][i]**2, 2 * timeSection[j][i], 1, 0],
                    [3 * timeSection[j][i + 1]**2, 2 * timeSection[j][i + 1], 1, 0]]
        
        vectorTGT[0] = targetPos[j][i]
        vectorTGT[1] = targetPos[j][i + 1]

        if j == 1:
            DesTrj.xTRJ[i] = matTRJ
            DesTrj.xTGT[0:2][i] = vectorTGT
        elif j == 2:
            DesTrj.yTRJ[i] = matTRJ
            DesTrj.yTGT[0:2][i] = vectorTGT
        elif j == 3:
            DesTrj.zTRJ[i] = matTRJ
            DesTrj.zTGT[0:2][i] = vectorTGT
        elif j == 4:
            DesTrj.rTRJ[i] = matTRJ
            DesTrj.rTGT[0:2][i] = vectorTGT
        elif j == 5:
            DesTrj.pTRJ[i] = matTRJ
            DesTrj.pTGT[0:2][i] = vectorTGT
        elif j == 6:
            DesTrj.hTRJ[i] = matTRJ
            DesTrj.hTGT[0:2][i] = vectorTGT


            

