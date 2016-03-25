# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:34:36 2016

@author: brian
"""

from math import exp, sqrt
import random

def LJ(r):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles    
    
    epsilon = 121.0
    sigma = 3.4    
    
    V = 4 * epsilon * ((sigma/r) ** 12 - (sigma/r) ** 6)    
    return V
    
    
def gradLJ(r):
    # The gradient of LJ

    epsilon = 121.0
    sigma = 3.4
    
    gV = 12 * epsilon * ((sigma/r) ** 6 - (sigma/r) ** 12) # *r(vector)/(r **2)
    return gV
    
    
def distance3(coord1, coord2):        
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2)
    
    return d
    

def distance4(coord1, coord2):        
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2 + (coord2[3] - coord1[3] ** 2))
    
    return d
    
    
def move3(step, coord):
    mX = coord[0] + (random.random() - 0.5) * step
    mY = coord[1] + (random.random() - 0.5) * step
    mZ = coord[2] + (random.random() - 0.5) * step
    
    return [mX, mY, mZ]
    
def move4(step, coord):
    mX = coord[0] + (random.random() - 0.5) * step
    mY = coord[1] + (random.random() - 0.5) * step
    mZ = coord[2] + (random.random() - 0.5) * step
    mW = coord[3] + (random.random() - 0.5) * step
    
    return [mX, mY, mZ, mW]
    

def transition(enDiff):
    # Currently treating Boltzmann constant as 1

    T = 35.0
    k = 1.0
    beta = 1/(k*T)
    
    if enDiff <= 0:
        return True
        
    else:
        R = random.random()
        W = exp(-beta * enDiff)
        
        if W > R:
            return True
        else:
            return False
            
            
class Particle:
    def __init__(self, num):
        self.num = num
        self.pos = [0,0,0]
        self.nPos = [0,0,0]
        
partList = []

for i in range(13):
    x = Particle(i+1)
    partList.append(x)    
    
for j in xrange(0, len(partList)):
    partList[j].pos.append(0)
    partList[j].nPos.append(0)
    partList[j].pos[0] = j+1
    print("Particle ", j+1, ":", partList[j].pos)    


def gradientDescent(x0):
    # Current non-stochastic method of minimization

    L = 0.1
    
    x1 = x0 - L * gradLJ(x0)
    
    return x1
    
    
def Walk(cycleNum):
    
    count = 0
    #step = 11.5 ** -9
    
    energy = []
    
    while count < cycleNum:
        initDist = {}        
                
        for i in partList:
            l = range(0, len(partList))
            l = l[:partList.index(i)] + l[partList.index(i)+1:]
            #print("L: ", l)
            for j in l:
                initDist[str(i.num) + " and " + str(partList[j].num)] = (distance4(i.pos, partList[j].pos))
                #print("Distance between ", partList.index(i)+1, "and ",
                j+1)
                #print(initDist[str(i.num) + " and " + str(partList[j].num)])
                
        en = 0
        for 
    
    return 

Walk(100)