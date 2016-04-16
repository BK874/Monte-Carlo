# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:13:04 2016

@author: brian
"""

from math import exp, sqrt
import random

def LJ(coord1, coord2):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles    
    
    r = distance3(coord1, coord2)
    epsilon = 121.0
    sigma = 3.4    
    
    V = 4 * epsilon * ((sigma/r) ** 12 - (sigma/r) ** 6)    
    return V
    
    
def deriv4LJ(coord1, coord2):
    # The derivative of LJ

    r = distance4(coord1, coord2)

    epsilon = 121.0
    sigma = 3.4

    dV = 24 * epsilon * ((sigma/r) ** 6 - 2 * (sigma/r) ** 12) * 1/r   
    return dV

def deriv3LJ(coord1, coord2):
    # The derivative of LJ

    r = distance3(coord1, coord2)

    epsilon = 121.0
    sigma = 3.4

    dV = 24 * epsilon * ((sigma/r) ** 6 - 2 * (sigma/r) ** 12) * 1/r   
    return dV

    
def distance4(coord1, coord2):       
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2 + (coord2[3] - coord1[3]) ** 2)   
    return d
 
 
def distance3(coord1, coord2):        
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2)
    
    return d
    

def deriv4DistX(coord1, coord2):
    # The derivative of the 4D distance formula w/respect to x

    d = (coord2[0] - coord1[0])/(distance4(coord1, coord2))
    return d
    
    
def deriv4DistY(coord1, coord2):
    # The derivative of the 4D distance formula w/respect to y

    d = (coord2[1] - coord1[1])/(distance4(coord1, coord2))
    return d
    

def deriv4DistZ(coord1, coord2):
    # The derivative of the 4D distance formula w/respect to z

    d = (coord2[2] - coord1[2])/(distance4(coord1, coord2))
    return d
    

def deriv4DistW(coord1, coord2):
    # The derivative of the 4D distance formula w/respect to w

    d = (coord2[3] - coord1[3])/(distance4(coord1, coord2))
    return d
    
def deriv3DistX(coord1, coord2):
    # The derivative of the 3D distance formula w/respect to x

    d = (coord2[0] - coord1[0])/(distance3(coord1, coord2))
    return d
    
    
def deriv3DistY(coord1, coord2):
    # The derivative of the 3D distance formula w/respect to y

    d = (coord2[1] - coord1[1])/(distance3(coord1, coord2))
    return d
    

def deriv3DistZ(coord1, coord2):
    # The derivative of the 3D distance formula w/respect to z

    d = (coord2[2] - coord1[2])/(distance3(coord1, coord2))
    return d
    

def grad4LJ(coord1, coord2):
    # The gradient of LJ

    gV = [(deriv4LJ(coord1, coord2) * deriv4DistX(coord1, coord2)), 
          (deriv4LJ(coord1, coord2) * deriv4DistY(coord1, coord2)),
          (deriv4LJ(coord1, coord2) * deriv4DistZ(coord1, coord2)),
          (deriv4LJ(coord1, coord2) * deriv4DistW(coord1, coord2))]
    return gV
    

def grad3LJ(coord1, coord2):
    # The gradient of LJ

    gV = [(deriv3LJ(coord1, coord2) * deriv3DistX(coord1, coord2)), 
          (deriv3LJ(coord1, coord2) * deriv3DistY(coord1, coord2)),
          (deriv3LJ(coord1, coord2) * deriv3DistZ(coord1, coord2))]
    return gV
    
        
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
numPart = 13

for i in range(numPart):
    x = Particle(i+1)
    partList.append(x)
    partList[i].pos[(partList[i].num-1)%3] = i+1    
    #print("Particle ", i+1, ":", partList[i].pos)
    

def gradientDescent(coord1, coord2, numCycle):
    # Current non-stochastic method of minimization

    L = 0.1 #????
    gdCount = 0
    x0 = [] 
    
    for n in xrange(3):
        x0.append(coord2[n] - coord1[n])
    
    #x1 = x0 - L * gradLJ(x0)
    while gdCount < numCycle:   
        temp = [L*m for m in grad3LJ([0,0,0],x0)]
        x1 = []
        for p in xrange(3):
            x1.append(x0[p] - temp[p])

        x0 = x1[:]            
        
        gdCount += 1
    
    return x0
    

def walk3(cycleNum):
    
    en = 0
    energy = []
    count = 0
    initDist = {}
    currDist = {}
    
    while count < cycleNum:
        
        for i in partList:
            for j in xrange(i.num+1, numPart+1):
                temp = []                
                for k in xrange(3):                
                    temp.append(partList[j-1].pos[k] - i.pos[k])
                    initDist[str(i.num) + " and " + str(j)] = temp
                
        for m in partList:
            for n in xrange(m.num+1, numPart+1):
                currDist[str(m.num) + " and " + str(n)] = gradientDescent([0,0,0], initDist[str(m.num) + " and " + str(n)], 1000)
        count += 1
        
    for p in partList:
        for q in xrange(p.num+1, numPart+1):
            en = LJ([0,0,0], currDist[str(p.num) + " and " + str(q)])
            energy.append(en)
    
    enTotal = 0
    for e in energy:
        enTotal += e
    return enTotal
    
print(walk3(100))

# Works consistently! Hooray!