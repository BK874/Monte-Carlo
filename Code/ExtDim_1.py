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

    gV = 24 * epsilon * ((sigma/r) ** 6 - 2 * (sigma/r) ** 12) * 1/r
    return gV
    
    
def distance3(coord1, coord2):        
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2)
    
    return d
    

def distance4(coord1, coord2):       
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2 + (coord2[3] - coord1[3]) ** 2)
    
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
numPart = 13

for i in range(numPart):
    x = Particle(i+1)
    partList.append(x)    
    
for j in xrange(0, numPart):
    partList[j].pos.append(0)
    partList[j].nPos.append(0)
    partList[j].pos[(partList[j].num-1)%3] = j+1
    #print("Particle ", j+1, ":", partList[j].pos)    


def gradientDescent(x0, numCycle):
    # Current non-stochastic method of minimization

    L = 0.1
    gdCount = 0
    
    while gdCount < numCycle:
    
        x0 = x0 - L * gradLJ(x0)
    
    return x0
    
    
def Walk(cycleNum): #add minimum parameter
    
    count = 0
    aCount = 0
    step = 3.4 # Distance parameter for LJ, otherwise: 11.5 ** -9
    energy = []
    
    initDist = {}
    currDist = {}

    
    while count < cycleNum:
                
        for i in partList:
            for j in xrange(i.num+1, numPart+1):
                #print("Part_1 pos: ",i.pos, "Part_2 pos: ",partList[j-1].pos)
                initDist[str(i.num) + " and " + str(j)] = distance4(i.pos, partList[j-1].pos)
                #print("Distance between ", partList.index(i)+1, "and ", j)
                #print(initDist[str(i.num) + " and " + str(j)])
        
        en = 0
        for k in xrange(1,numPart+1):
            for l in xrange(k+1, numPart+1):
                #print(k, " and ", l)
                en += LJ(initDist[str(k) + " and " + str(l)])
            
        if count == 0:
            energy.append(en)
        
        for m in partList:
            m.nPos = move4(step, m.pos)
            for n in xrange(m.num+1, numPart+1):
                currDist[str(m.num) + " and " + str(n)] = distance4(m.pos, partList[n-1].pos)
                
        nEn = 0
        for p in xrange(1, numPart+1):
            for q in xrange(k+1, numPart+1):
                nEn += LJ(currDist[str(p) + " and " + str(q)])
                
        enDiff = nEn - en
        
        t = transition(enDiff)

        if t == True:
            for r in partList:
                r.pos = r.nPos
            energy.append(nEn)
            aCount += 1
            
        else:
            for s in partList:
                s.nPos = s.pos
            energy.append(en)
                         
             
        count += 1
    
    enTotal = 0
    for en in energy:
        enTotal += en
    avgEn = enTotal/cycleNum
    print("The average energy was: ", avgEn)
    #print("The number of accepted moves was: ", aCount)
    #print("The ratio of acceptance was: ", aCount/cycleNum)
    return avgEn    
    
    return 

Walk(100)