# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:07:45 2016

@author: brian
"""

import sys
sys.path.append('/usr/share/pyshared')
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import constants as con
from math import exp
import random

expResult = 0.5 * con.k * 400

def Harmonic(x):
    a = 1#0 ** -21
    U = (0.5) * a * (x ** 2)    
    
    return U

def Metropolis(cycleNum):
    count = 0
    aCount = 0
    upStep = 0
    T = 400
    beta = 1.0 /(con.k * T)
    step = 11.5 ** -9 # gives about 47.5% acceptance w/T = 400
    initPoint = 0 #random.uniform(-10.0, 10.0)
    point = initPoint
    
    expResult = 0.5 * con.k * T
    
    position = []
    energy = []
    
    while count < cycleNum:
        initEnergy = Harmonic(point)
        displace = (random.random() - 0.5) * step
        
        newPoint = point + displace
        newEnergy = Harmonic(newPoint)
        enDiff = newEnergy - initEnergy
        #print("-------")
        #print("Negative beta: ", -beta)
        #print("Energy difference: ", enDiff)
        #print("-beta * energy difference: ", -beta * enDiff)

        if enDiff <= 0:
            point = newPoint
            position.append(point)
            energy.append(newEnergy)
            
        else:
            R = random.random()
            W = exp(-beta * enDiff)
            #print("W: ", W)
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
    print("The average energy was: ", avgEn)# * con.k * T)
    print("The number of potential steps up was: ", upStep)
    print("The number of accepted steps up was: ", aCount)
    print("The expected energy result is: ", expResult)

    
    return avgEn
    
Metropolis(10000)