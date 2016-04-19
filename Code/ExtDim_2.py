# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:13:04 2016

@author: brian
"""

from math import exp, sqrt
import numpy as np
import random
import time

def LJ(coord1, coord2):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles    
    
    r = distance3(coord1, coord2)
    if r == 0:
        return 0    
    
    epsilon = 121.0
    sigma = 3.4    
    
    V = 4 * epsilon * ((sigma/r) ** 12 - (sigma/r) ** 6)    
    return V
    
def LJ2(r):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles    
    
    if r == 0:
        return 0
    
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
        self.tempPos = [0,0,0]
        self.nPos = [0,0,0]
        self.pos3 = [0,0,0]
        
    
def extension():
    for j in range(numPart):
        partList[j].pos.append(0)
        partList[j].tempPos.append(0)
        partList[j].nPos.append(0)
        
def rExtension():
    for k in range(numPart):
        del partList[k].pos[-1]
        del partList[k].tempPos[-1]
        del partList[k].nPos[-1]
        
def set3d():
    for p in xrange(0, numPart):
        for c in xrange(3):
            partList[p].pos3[c] = partList[p].pos[c]      
    return
    
def perpVect(step, v):    
    
    r = 0.1 * step
    vTemp = list(v)
    v3 = v.pop(3)
    v4 = []
    if vTemp[1] == 0 and vTemp[2] == 0:
        if vTemp[0] == 0 and vTemp[3]:
            raise ValueError('zero vector')
        else:
            v4 = list(np.cross(v, [0, r, 0]))
            v4.append(v3)
            v.append(v3)
            #print(v4)
            return v4
    c = random.randint(0, 2)
    nV = [0, 0, 0]
    nV[c] = r        
    v4 = list(np.cross(v, nV))
    #print(v4)
    v4.append(v3)
    v.append(v3)
    return v4
    

def find3DEnergy():
    e0 = 0
    
    for v in partList:
        for w in xrange(v.num+1, numPart+1):
            dist = distance4(v.pos3, partList[w-1].pos3)
            e0 += LJ2(dist)
    return e0

def gradFX():
    
    e0 = find3DEnergy()
    gF = []
    
    return
        

def compression():
    
    success = False
    
    
        
                
    
    return success
    

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
    start_time = time.time()
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
                    initDist[str(i.num) + " and " + str(j)] = list(temp)
                
        for m in partList:
            for n in xrange(m.num+1, numPart+1):
                currDist[str(m.num) + " and " + str(n)] = gradientDescent([0,0,0], initDist[str(m.num) + " and " + str(n)], 100)
        count += 1
        
    for p in partList:
        for q in xrange(p.num+1, numPart+1):
            en = LJ([0,0,0], currDist[str(p.num) + " and " + str(q)])
            energy.append(en)
    
    enTotal = 0
    for e in energy:
        enTotal += e

    for r in partList:
        for s in xrange(r.num+1, numPart+1):
            r.pos = list(currDist[str(r.num) + " and " + str(s)])  
    
    print("---Walk3: %s seconds ---" % (time.time() - start_time))
            
    return enTotal

def extWalk(cycleNum):
    start_time = time.time()
    
    count = 0
    aCount = 0
    step = 3.4 # Distance parameter for LJ, otherwise: 11.5 ** -9
    #energy = []
    
    initDist = {}
    currDist = {}

    while count < cycleNum:
        
        for i in partList:
            for j in xrange(i.num+1, numPart+1):
                initDist[str(i.num) + " and " + str(j)] = distance4(i.pos, partList[j-1].pos)
                
        en = 0
        for k in xrange(1,numPart+1):
            for l in xrange(k+1, numPart+1):
                #print(initDist[str(k) + " and " + str(l)])
                en += LJ2(initDist[str(k) + " and " + str(l)])
                
        for r in partList:
            r.tempPos = list(r.pos)
            
        for m in partList:
            gE = [0, 0, 0, 0]
            for t in xrange(m.num+1, numPart+1):
                gEp = grad4LJ(m.pos, partList[t-1].pos)
                for u in range(4):
                    gE[u] += gEp[u]
            pV = list(perpVect(step, gE))
            for s in range(4):
                m.nPos[s] = m.pos[s] + pV[s]
            for n in xrange(m.num+1, numPart+1):
                currDist[str(m.num) + " and " + str(n)] = distance4(m.nPos, partList[n-1].tempPos)
            m.tempPos = list(m.nPos)
        
                
        nEn = 0
        for p in xrange(1, numPart+1):
            for q in xrange(p+1, numPart+1):
                nEn += LJ2(currDist[str(p) + " and " + str(q)])
        
        #print("En ", en, "nEn", nEn)
        enDiff = nEn - en              
                
        t = transition(enDiff)

        if t == True:
            for r in partList:
                r.pos = list(r.nPos)
            en = nEn
            aCount += 1
            
        else:
            for s in partList:
                s.nPos = list(s.pos)
            #energy.append(en)
                         
             
        count += 1
    
    #print("aCount: ", aCount)
    print("---ExtWalk: %s seconds ---" % (time.time() - start_time))
    return en
    
start_time = time.time()

partList = []
numPart = 16

for i in range(numPart):
    x = Particle(i+1)
    partList.append(x)
    partList[i].pos[(partList[i].num-1)%3] = i+1    
    #print("Particle ", i+1, ":", partList[i].pos)

count = 10
cycleNum = 0


walk3(100)
while cycleNum < count:

        set3d()
        extension()
        extWalk(100)
        rExtension()
        print(walk3(100))
        
        cycleNum += 1

print("--- %s seconds ---" % (time.time() - start_time))

# Need to write compression function