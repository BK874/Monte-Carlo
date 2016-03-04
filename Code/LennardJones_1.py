# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:35:39 2016

@author: brian
"""

#import sys
#sys.path.append('/usr/share/pyshared')

# Necessary imports
from math import exp
from math import sqrt
import random

# Function for the Lennard-Jones potential
def LennardJones(r):
    # v = 4 * epsilon * ((sigma/r)^12 - (sigma/r)^6)
    # epsilon = depth of the potential well
    # sigma = finite distance at which the inter-particle potential is zero
    # r = distance between particles

    # Currently keeping variables at 1
    epsilon = 121
    sigma = 3.4
    
    V = 4 * epsilon * ((sigma/r) ** 12 - (sigma/r) ** 6)
    
    #print V

    return V
    

# Function for the distance formula in three dimensions    
def distance(x2, x1, y2, y1, z2, z1):
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return d
    

# Class for the particles    
class Particle:
    
    def __init__(self, num):
        self.num = num
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.nx = 0
        self.ny = 0
        self.nz = 0
    

# Declare and initialize 3 particles (would like to create a more 
# general method for delclaring a variable number of particles)
p1 = Particle(1)
p1.x = 1
p2 = Particle(2)
p2.y = 1
p3 = Particle(3)
p3.z= 1
    

# Function for calculating the distance between two particles - tried to
# make it general, will become more complicated as more particles are 
# added    
def partDist(part1, part2, x):
    
    # Accepts three parameters: the numbes of the two particles and 1 or 2
    # -> 1 means the distance is calculated using the new coordinates
    # -> 2 means the distance is calculated using the old coordinates

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


        
# Function for calculating the probability of accepting new states
def transition(enDiff):
    # Currently treating the boltzmann constant as 1
    # Temperature is set to 20    
    
    T = 20.0
    k = 1.0
    beta = 1/(k * T)
    
    if enDiff <= 0:
        return True
        
    else:
        R = random.random()
        W = exp(-beta * enDiff)
        print("W: ", W)
        
        if W > R:
            return True
            
        else:
            return False
    

# The Metropolis algorithm function
def Metropolis(cycleNum):
    # The parameter is the number of cycles it will run    
    
    # Declare and initialize the cycle counter and the step size
    count = 0.0
    aCount = 0
    step = 0.249 #11.5 ** -9 # A guess based off of my working Harmonic code
    
    # A list for averaging the energy
    energy = []
    
    # Calculate the initial distances between the particles
    dist_1_2 = partDist(1, 2, 2)
    dist_1_3 = partDist(1, 3, 2)
    dist_2_3 = partDist(2, 3, 2)
    #print dist_1_2
    #print dist_1_3
    #print dist_2_3
    
    # While loop - runs the algorithm for the specified number of cycles
    while count < cycleNum:
        # For each particle the initial energy between the other particles
        # is calculated.
        # Next the displacement is generated and applied to the x, y, z
        # coordinates
        # The new distances and energies are calculated
        # The difference in the new and initial energies is then 
        # calculated and ran through the transition function
        
        # Particle 1 
        en_1_2 = LennardJones(dist_1_2)
        en_1_3 = LennardJones(dist_1_3)
        
        displace = (random.random() - 0.5) * step                
        p1.nx = p1.x + displace
        
        displace = (random.random() - 0.5) * step
        p1.ny = p1.y + displace
    
        displace = (random.random() - 0.5) * step
        p1.nz = p1.z + displace
        
        ndist_1_2 = partDist(1, 2, 1)
        ndist_1_3 = partDist(1, 3, 1)
        
        nen_1_2 = LennardJones(ndist_1_2)
        nen_1_3 = LennardJones(ndist_1_3)
        
        enDiff_1 = (nen_1_2 - en_1_2) + (nen_1_3 - en_1_3)
        
#        if transition(enDiff) == True:
#            dist_1_2 = ndist_1_2
#            dist_1_3 = ndist_1_3
#            p1.x = p1.nx
#            p1.y = p1.ny
#            p1.z = p1.nz
#            energy.extend([nen_1_2, nen_1_3])
            
#        else:
#            energy.extend([en_1_2, en_1_3])
#            p1.nx = p1.x
#            p1.ny = p1.y
#            p1.nz = p1.z
            
        # Particle 2 
        en_1_2 = LennardJones(dist_1_2)
        en_2_3 = LennardJones(dist_2_3)
        
        displace = (random.random() - 0.5) * step        
        p2.nx = p1.x + displace
        displace = (random.random() - 0.5) * step       
        p2.ny = p2.y + displace
        displace = (random.random() - 0.5) * step       
        p2.nz = p2.z + displace
            
        ndist_1_2 = partDist(1, 2, 1)
        ndist_2_3 = partDist(2, 3, 1)
        
        nen_1_2 = LennardJones(ndist_1_2)
        nen_2_3 = LennardJones(ndist_2_3)
        
        enDiff_2 = (nen_1_2 - en_1_2) + (nen_2_3 - en_2_3)
        
#        if transition(enDiff) == True:
#            dist_1_2 = ndist_1_2
#            dist_2_3 = ndist_2_3
#            p2.x = p2.nx
#            p2.y = p2.ny
#            p2.z = p3.nz
#            energy.extend([nen_1_2, nen_2_3])
            
 #       else:
#            energy.extend([en_1_2, en_2_3])
#            p2.nx = p2.x
#            p2.ny = p2.y
#            p2.nz = p2.z
            
        # Particle 3
        en_1_3 = LennardJones(dist_1_3)
        en_2_3 = LennardJones(dist_2_3)
        
        displace = (random.random() - 0.5) * step       
        p3.nx = p3.x + displace
        displace = (random.random() - 0.5) * step       
        p3.ny = p3.y + displace
        displace = (random.random() - 0.5) * step       
        p3.nz = p3.z + displace
            
        ndist_1_3 = partDist(1, 3, 1)
        ndist_2_3 = partDist(2, 3, 1)
        
        nen_1_3 = LennardJones(ndist_1_3)
        nen_2_3 = LennardJones(ndist_2_3)
        
        enDiff_3 = (nen_1_3 - en_1_3) + (nen_2_3 - en_2_3)
        
        enDiff = enDiff_1 + enDiff_2 + enDiff_3        

        
        if transition(enDiff) == True:

            dist_1_2 = ndist_1_2
            dist_1_3 = ndist_1_3
            p1.x = p1.nx
            p1.y = p1.ny
            p1.z = p1.nz
            energy.extend([nen_1_2, nen_1_3])            

            dist_1_2 = ndist_1_2
            dist_2_3 = ndist_2_3
            p2.x = p2.nx
            p2.y = p2.ny
            p2.z = p3.nz
            energy.extend([nen_1_2, nen_2_3])
            
            dist_1_3 = ndist_1_3
            dist_2_3 = ndist_2_3
            p3.x = p3.nx
            p3.y = p3.ny
            p3.z = p3.nz
            energy.extend([nen_1_3, nen_2_3])
            
            aCount += 1
            
        else:
            
            energy.extend([en_1_2, en_1_3])
            p1.nx = p1.x
            p1.ny = p1.y
            p1.nz = p1.z

            energy.extend([en_1_2, en_2_3])
            p2.nx = p2.x
            p2.ny = p2.y
            p2.nz = p2.z            
            
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
    print("The number of accepted moves was: ", aCount)
    return avgEn
    

Metropolis(100000.0)