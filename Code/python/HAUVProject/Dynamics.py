import tensorflow as tf
import numpy as np

""" Notation 
    vPosEF: Position and orientation of HAUV [m], [rad] - u1 ~ u6
    vVelBF: Velocity and Acceleration of HAUV [m/s], [rad/s] - u7 ~ u12
    vTBF  : Force and Moment acting on HAUV (thruster) [N] - u13 ~ u18
    cVelBF: Velocity Vector of current (BF) [m/s] - u19 ~ u21
    cVelEF: Velocity Vector of current (EF) [m/s] - u22 ~ u24
"""

class Dynamics(object):
    def __init__(self):
        pass

    def IntertialMatrix(self):
        matMRB = np.zeros((6, 6))
        matMRB[0][0]



    def HauvDynamics(self):
        pass
