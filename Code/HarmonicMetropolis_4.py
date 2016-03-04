# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:26:03 2016

@author: brian
"""

# Harmonic Metropolis 4 - auto/manual adjust step size
# while running.

#import sys
#sys.path.append('/usr/share/pyshared')
#import matplotlib as mpl
#import matplotlib.pyplot as plt
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
    aCount = 0.0
    upStep = 0.0
    downAdjust = 0
    upAdjust = 0
    T = 400
    beta = 1.0 /(con.k * T)
    step = 11.5 ** -9 # gives about 47.5% acceptance w/T = 400
    stepBase = 11.5
    stepMag = -9
    initPoint = 0 #random.uniform(-10.0, 10.0)
    point = initPoint
    
    expResult = 0.5 * con.k * T
    
    position = []
    energy = []
    
    while count < cycleNum:
        initEnergy = Harmonic(point)
        displace = (random.random() - 0.5) * (stepBase ** stepMag)
        
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
                
        if count > cycleNum * 0.01: #and count < cycleNum * 0.9:
            if aCount/upStep < 0.47:
                #print(aCount/upStep)
                #print("Auto adjusting step size (acceptance below)")
                stepBase += 0.05
                upAdjust += 1
            
            elif aCount/upStep > 0.53:
                #print(aCount/upStep)
                #print("Auto adjusting step size (acceptance above)")
                stepBase -= 0.01
                downAdjust += 1
                
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
    print("The percent of accepted moves was: ", aCount/upStep)
    print("The number of step increases was: ", upAdjust)
    print("The number of step decreases was: ", downAdjust)
    print("The final step size was: ", stepBase, " ** ", stepMag)
    print("The expected energy result is: ", expResult)

    
    return avgEn
    
Metropolis(10000)
    