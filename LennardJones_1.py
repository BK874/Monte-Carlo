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
    
    #print V

    return V
    
    
def distance(x2, x1, y2, y1, z2, z1):
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return d
    
    
class Particle:
    
    def __init__(self, num):
        self.num = num
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.nx = 0
        self.ny = 0
        self.nz = 0
    

p1 = Particle(1)
p1.x = 1
p2 = Particle(2)
p2.y = 1
p3 = Particle(3)
p3.z= 1
    
    
def partDist(part1, part2, x):

    if x == 1:
        if part1 + part2 == 3:
            d = distance(p2.nx, p1.nx, p2.ny, p1.ny, p2.nz, p1.nz)
        elif part1 + part2 == 4:
            d = distance(p3.nx, p1.nx, p3.ny, p1.ny, p3.nz, p1.nz)
        elif part1 + part2 == 5:
            d = distance(p3.nx, p2.nx, p3.ny, p2.ny, p3.nz, p2.nz)

    elif x == 2:
        if part1 + part2 == 3:
            d = distance(p2.x, p1.x, p2.y, p1.y, p2.z, p1.z)
        elif part1 + part2 == 4:
            d = distance(p3.x, p1.x, p3.y, p1.y, p3.z, p1.z)
        elif part1 + part2 == 5:
            d = distance(p3.x, p2.x, p3.y, p2.y, p3.z, p2.z)
            
    return d
        
def transition(enDiff):
    T = 100
    k = 1
    beta = 1/(k * T)
    
    if enDiff <= 0:
        return True
        
    else:
        R = random.random()
        W = exp(-beta * enDiff)
        
        if W > R:
            return True
            
        else:
            return False
    

def Metropolis(cycleNum):
    count = 0
    step = 11.5 ** -9 # A guess based off of my working Harmonic code
    
    energy = []
    
    dist_1_2 = partDist(1, 2, 2)
    dist_1_3 = partDist(1, 3, 2)
    dist_2_3 = partDist(2, 3, 2)
    #print dist_1_2
    #print dist_1_3
    #print dist_2_3
    
    while count < cycleNum:
        
        # Particle 1 
        en_1_2 = LennardJones(dist_1_2)
        en_1_3 = LennardJones(dist_1_3)
        displace = (random.random() - 0.5) * step
        #print displace
        
        p1.nx = p1.x + displace
        #print(p1.nx)
        p1.ny = p1.y + displace
        #print(p1.ny)
        p1.nz = p1.z + displace
        #print(p1.nz)
        
        ndist_1_2 = partDist(1, 2, 1)
        ndist_1_3 = partDist(1, 3, 1)
        
        nen_1_2 = LennardJones(ndist_1_2)
        nen_1_3 = LennardJones(ndist_1_3)
        
        enDiff = (nen_1_2 - en_1_2) + (nen_1_3 - en_1_3)
        
        if transition(enDiff) == True:
            dist_1_2 = ndist_1_2
            dist_1_3 = ndist_1_3
            p1.x = p1.nx
            p1.y = p1.ny
            p1.z = p1.nz
            energy.extend([nen_1_2, nen_1_3])
            
        else:
            energy.extend([en_1_2, en_1_3])
            p1.nx = p1.x
            p1.ny = p1.y
            p1.nz = p1.z
            
        # Particle 2 
        en_1_2 = LennardJones(dist_1_2)
        en_2_3 = LennardJones(dist_2_3)
        
        displace = (random.random() - 0.5) * step
        
        p2.nx = p1.x + displace
        p2.ny = p2.y + displace
        p2.nz = p2.z + displace
            
        ndist_1_2 = partDist(1, 2, 1)
        ndist_2_3 = partDist(2, 3, 1)
        
        nen_1_2 = LennardJones(ndist_1_2)
        nen_2_3 = LennardJones(ndist_2_3)
        
        enDiff = (nen_1_2 - en_1_2) + (nen_2_3 - en_2_3)
        
        if transition(enDiff) == True:
            dist_1_2 = ndist_1_2
            dist_2_3 = ndist_2_3
            p2.x = p2.nx
            p2.y = p2.ny
            p2.z = p3.nz
            energy.extend([nen_1_2, nen_2_3])
            
        else:
            energy.extend([en_1_2, en_2_3])
            p2.nx = p2.x
            p2.ny = p2.y
            p2.nz = p2.z
            
        # Particle 3
        en_1_3 = LennardJones(dist_1_3)
        en_2_3 = LennardJones(dist_2_3)
        
        displace = (random.random() - 0.5) * step
        
        p3.nx = p3.x + displace
        p3.ny = p3.y + displace
        p3.nz = p3.z + displace
            
        ndist_1_3 = partDist(1, 3, 1)
        ndist_2_3 = partDist(2, 3, 1)
        
        nen_1_3 = LennardJones(ndist_1_3)
        nen_2_3 = LennardJones(ndist_2_3)
        
        enDiff = (nen_1_3 - en_1_3) + (nen_2_3 - en_2_3)
        
        if transition(enDiff) == True:
            dist_1_3 = ndist_1_3
            dist_2_3 = ndist_2_3
            p3.x = p3.nx
            p3.y = p3.ny
            p3.z = p3.nz
            energy.extend([nen_1_3, nen_2_3])
            
        else:
            energy.extend([en_1_3, en_2_3])
            p3.nx = p3.x
            p3.ny = p3.y
            p3.nz = p3.z
            
        count += 1
        
        
    enTotal = 0
    for en in energy:
        enTotal += en
    avgEn = enTotal/cycleNum
    print("The average energy was: ", avgEn)
    
    return avgEn
    

Metropolis(100000)