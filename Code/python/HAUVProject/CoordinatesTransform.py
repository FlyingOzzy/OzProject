import tensorflow as tf
import numpy as np
import pandas as pd
import pywt
import math as m


""" Input ([12 x 1] Vector) 
vPos = [u(01); u(02); ...; u(06)] : Position and Orientation of the HAUV [m] and [rad]
vVel = [u(07); u(08); ...; u(12)] : Velocity and Angular Velocity of the HAUV [m/s] and [rad/s]
"""

""" Class """ 

class TransCoord(object):
    def __init__(self):
        pass

    def TransMatLinear(self, phi, theta, psi):
        roMat = np.zeros((3, 3))
    
        roMat[0, 0] = m.cos(theta) * m.cos(psi)
        roMat[0, 1] = -(m.cos(phi)) * m.sin(psi) + m.sin(phi) * m.sin(theta) * m.cos(psi)
        roMat[0, 2] = m.sin(phi) * m.sin(psi) + m.cos(phi) * m.sin(theta) * m.cos(psi)
    
        roMat[1, 0] = m.cos(theta) * m.sin(psi)
        roMat[1, 1] = m.cos(phi) * m.cos(psi) + m.sin(phi) * m.sin(theta) * m.sin(psi)
        roMat[1, 2] = -(m.sin(phi)) * m.cos(psi) + m.cos(phi) * m.sin(theta) * m.sin(psi)
    
        roMat[2, 0] = -(m.sin(theta))
        roMat[2, 1] = m.sin(phi) * m.cos(theta)
        roMat[2, 2] = m.cos(phi) + m.cos(theta)
    
        return roMat

    def TransMatAng(self, phi, theta, psi):
        roMat = np.zeros((3, 3))
    
        roMat[0, 0] = 1
        roMat[0, 1] = m.sin(phi) * m.tan(theta)
        roMat[0, 2] = m.cos(phi) * m.tan(theta)
    
        roMat[1, 0] = 0
        roMat[1, 1] = m.cos(phi)
        roMat[1, 2] = -(m.sin(phi))
    
        roMat[2, 0] = 0
        roMat[2, 1] = m.sin(phi) / m.cos(theta)
        roMat[2, 2] = m.cos(phi) / m.cos(theta)
    
        return roMat


""" Main routine """

if __name__ == '__main__':
    Tcoord = TransCoord()
    
    a = Tcoord.TransMatLinear(40, 60, 30)
    print(a)
    b = Tcoord.TransMatAng(40, 60, 30)
    print(b)
    
    
    
