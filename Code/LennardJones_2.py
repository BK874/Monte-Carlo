# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:57:53 2016

@author: brian
"""

from math import exp, sqrt
import random


# Lennard Jones Potential
def LJ(r):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles    
    
    epsilon = 121.0
    sigma = 3.4    
    
    V = 4 * epsilon * ((sigma/r) ** 12 - (sigma/r) ** 6)    
    return V

# Distance Function    
def distance(coord1, coord2):        
    d = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + 
    (coord2[2] - coord1[2]) ** 2)
    
    return d
    
# Movement Function    
def move(step, coord):
    mX = coord[0] + (random.random() - 0.5) * step
    mY = coord[1] + (random.random() - 0.5) * step
    mZ = coord[2] + (random.random() - 0.5) * step
    
    return [mX, mY, mZ]

# Transition Function    
def transition(enDiff):
    # Currently treating Boltzmann constant as 1

    T = 35.0
    k = 1.0
    beta = 1/(k*T)
    
    #print("enDiff: ", enDiff)
    
    if enDiff <= 0:
        #print("Down!")
        return True
        
    else:
        R = random.random()
        W = exp(-beta * enDiff)
        #print("W: ", W)
        #print("R: ", R)
        
        if W > R:
            #print("Accepted up!")
            return True
        else:
            #print("No!")
            return False
    
# Particle Class
# Upon creation is assigned a number
# Also contains lists for its current position and possible new position       
class Particle:
    def __init__(self, num):
        self.num = num
        self.pos = [0,0,0]
        self.nPos = [0,0,0]
        

# Declare and initialize 3 particles (would like to create a more 
# general method for delclaring a variable number of particles)
p1 = Particle(1)
p1.pos[0] = 1.0
p1.nPos[0] = 1.0
p2 = Particle(2)
p2.pos[1] = 1.0
p2.nPos[1] = 1.0
p3 = Particle(3)
p3.pos[2] = 1.0
p3.nPos[2]=1.0

# Metropolis function
def Metropolis(cycleNum):
    
    count = 0
    aCount = 0
    step = 11.5**-9
    
    # Create a list for storing the energy
    energy = []
        
    while count < cycleNum:
        # Calculate the initial distance between the particles
        r12 = distance(p1.pos, p2.pos)
        r13 = distance(p1.pos, p3.pos)
        r23 = distance(p2.pos, p3.pos)
        #print("r12, r13, r23: ", r12, r13, r23)
        # Calculate the initial energy and add it to the list
        en = LJ(r12) + LJ(r13) + LJ(r23)
        #print("en: ", en)
        if count == 0:
            energy.append(en)        
        
        p = random.randint(1,3)
        
        if p == 1:
            p1.nPos = move(step, p1.pos)
            r12 = distance(p1.nPos, p2.pos)
            r13 = distance(p1.nPos,p3.pos)
        elif p == 2:
            p2.nPos = move(step, p2.pos)
            r12 = distance(p2.nPos, p1.pos)
            r13 = distance(p2.nPos, p3.pos)
        elif p == 3:
            p3.nPos = move(step, p3.pos)
            r13 = distance(p3.nPos, p1.pos)
            r23 = distance(p3.nPos, p2.pos)
        
        nEn = LJ(r12) + LJ(r13) + LJ(r23)
        #print("nEn: ", nEn)        
        enDiff = nEn - en
    
        t = transition(enDiff)

        if t == True:
            p1.pos = p1.nPos
            p2.pos = p2.nPos
            p3.pos = p3.nPos
            energy.append(nEn)
            aCount += 1
            
        else:
            p1.nPos = p1.pos
            p2.nPos = p2.pos
            p3.nPos = p3.pos
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
    

Metropolis(100000.0)
# Create list of particles and use for loop/indexing to create the particles 
#i.e. for j < 13, particles[j] = foo
# See Prof. Laboon's StaticDemo example (assuming he updated it)