# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:08:44 2016

@author: brian
"""

import sys
sys.path.append('/usr/share/pyshared')
#import matplotlib as mpl
#import matplotlib.pyplot as plt
from scipy import constants as con
from math import exp
import random

def Morse(r):
    De = 142.9 # kB * K
    a = 1.691 # Å^-1
    re = 3.762 # Å
    
    U = De * (exp(-2 * a * (r - re)) - 2 * exp(-a * (r - re)))
    
    return U
    
def Metropolis(cycleNum):
    count = 0
    aCount = 0
    upStep = 0
    T = 100
    beta = 1.0 /T# (con.k * T)
    step = 0.004 #** -9 # gives about 47% acceptance w/T = 400
    initPoint = 0 #random.uniform(-10.0, 10.0)
    point = initPoint
    
    position = []
    energy = []
    
    while count < cycleNum:
        initEnergy = Morse(point)
        displace = (random.random() - 0.5) * step
        
        newPoint = point + displace
        newEnergy = Morse(newPoint)
        
        enDiff = newEnergy - initEnergy
        
        if enDiff < 0:
            point = newPoint
            position.append(point)
            energy.append(newEnergy)
            
        else:
            R = random.random()
            W = exp(-beta * enDiff)
            upStep += 1
            
            if W > R:
                point = newPoint
                position.append(point)
                energy.append(newEnergy)
                aCount += 1
                
            else:
                position.append(point)
                energy.append(initEnergy)
                
        count += 1
        
    posTotal = 0
    for pos in position:
        posTotal += pos
    avgPos = posTotal/cycleNum
    
    enTotal = 0
    for en in energy:
        enTotal += en
    avgEn = enTotal/cycleNum
    

    print("The average position was: ", avgPos)
    print("The average energy was: ", avgEn * con.k) #* T)
    print("The number of potential steps up was: ", upStep)
    print("The number of accepted steps up was: ", aCount)

    
    return avgEn
    
Metropolis(10000)

# Consistent results achieved. No idea if they are correct though
# Is it correct to remove the Boltzmann constants until the end
# but leave the temperature?    