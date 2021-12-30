import tensorflow as tf
import numpy as np
import math as m

class Control(object):
    def __init__(self):
        self.quadrant = 1
        self.nRevolution = 0     # revolution
        self.ctrlType = 'SMC'    # Sliding Mode
        self.preDesiredPsi = 0

    
