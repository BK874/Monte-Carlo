# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:35:39 2016

@author: brian
"""

import sys
sys.path.append('/usr/share/pyshared')
#from scipy import constants as con
from math import exp
from math import sqrt
import random

def LennardJones(r):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles

    epsilon = 1
    sigma = 1
    
    V = 4 * epsilon * ((sigma/r) ** 12 - (sigma/r) ** 6)
    
    return V
    
def Distance(x2, x1, y2, y1, z2, z1):
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return d
    
def Metropolis(partNum, cycleNum):
    count = 0
    T = 100
    k = 1
    beta = 1/(k * T)
    step = 11.5 ** -9 # A guess based off of my working Harmonic code
    initPoint = 0 # Can be changed to a random number
    point = initPoint
    
    while count < cycleNum:
        
        for particle in partNum:
            
        
            