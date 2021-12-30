from CoordinatesTransform import *

import numpy as np
import tensorflow as tf

class DesiredTrajectory(object):
    def __init__(self):
        self.tgtPos = np.zeros((6, 4))

        self.xTRJ = np.zeros((4, 4, len(self.tgtPos) - 1))
        self.xTGT = np.zeros((4, len(self.tgtPos) - 1))

        self.yTRJ = np.zeros((4, 4, len(self.tgtPos) - 1))
        self.yTGT = np.zeros((4, len(self.tgtPos) - 1))
        
        self.zTRJ = np.zeros((4, 4, len(self.tgtPos) - 1))
        self.zTGT = np.zeros((4, len(self.tgtPos) - 1))

        self.rTRJ = np.zeros((4, 4, len(self.tgtPos) - 1))
        self.rTGT = np.zeros((4, len(self.tgtPos) - 1))

        self.pTRJ = np.zeros((4, 4, len(self.tgtPos) - 1))
        self.pTGT = np.zeros((4, len(self.tgtPos) - 1))

        self.hTRJ = np.zeros((4, 4, len(self.tgtPos) - 1))
        self.hTGT = np.zeros((4, len(self.tgtPos) - 1))

        self.tCoord = TransCoord()


    def DesTrajectory(self, t, timeSection, tgtPos):
        indexTraj = np.zeros((6, 1))
    
        for i in range(6):
            if (t >= timeSection(i, 0) and t < timeSection(i, 1)):
                indexTraj[i] = 1
            
            elif (t >= timeSection(i, 1) and t < timeSection(i, 2)):
                indexTraj[i] = 2
            
            else:
                indexTraj[i] = 3

        Cx = np.linarg.solve(self.xTRJ[:, :, indexTraj[0]], self.xTGT[:, indexTraj[0]])
        Cy = np.linarg.solve(self.yTRJ[:, :, indexTraj[1]], self.yTGT[:, indexTraj[1]])
        Cz = np.linarg.solve(self.zTRJ[:, :, indexTraj[2]], self.zTGT[:, indexTraj[2]])
        Cr = np.linarg.solve(self.rTRJ[:, :, indexTraj[3]], self.rTGT[:, indexTraj[3]])
        Cp = np.linarg.solve(self.pTRJ[:, :, indexTraj[4]], self.pTGT[:, indexTraj[4]])
        Ch = np.linarg.solve(self.hTRJ[:, :, indexTraj[5]], self.hTGT[:, indexTraj[5]])
    
        matC = [Cx, Cy, Cz, Cr, Cp, Ch]

        desPosEF = matC.T * [t**3, t**2, t, 1] 
        desVelEF = matC.T * [3 * t**2, 2 * t, 1, 0]
        desAccEF = matC.T * [6 * t, 1, 0, 0]

        phi = desPosEF[3]
        theta = desPosEF[4]
        psi = desPosEF[5]

        linMat = self.tCoord.TransMatLinear(phi, theta, psi)
        angMat = self.tCoord.TransMatAng(phi, theta, psi)

        linVelBF = linMat.T * desVelEF[0 : 3]
        angVelBF = np.linarg.solve(angMat, desVelEF[3 : 6])

        desVelBF = [linVelBF, angVelBF]

        return desVelBF


if __name__ == "__main__":
    DesTraj = DesiredTrajectory()



