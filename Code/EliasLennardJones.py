import random
import math

# moves the particle
    # param displace: multiplier for displacement
    # param coord: array of starting coordinates
    # returns array of moved particle
def move( maxDis, coord ):
    disX = coord[0] + maxDis*(random.random() - .5)
    disY = coord[1] + maxDis*(random.random() - .5)
    disZ = coord[2] + maxDis*(random.random() - .5)
    return [disX, disY, disZ];
    
#calculates the change in energy
    # 4(r^-12-r^-6) = potential
    # param current: energy at the given time
    # param r: distance between particles
    # returns change in energy
def energyCalc(r):
    return 4*eps*((sigma/r)**12-(sigma/r)**6)
    
    
#calculates distance between particles
    # param coord1: numpy array of coordinates start pos
    # param coord2: end pos
    # return distance between to coordinates
def distance(coord1, coord2):
    return math.sqrt((coord2[0]-coord1[0])**2+(coord2[1]-coord1[1])**2+(coord2[2]-coord1[2])**2)
    #return np.linalg.norm(coord1-coord2)


#### Parameters ####
maxDis = 11.5**-9 # displacement multiplier
sigma = 3.4
eps = 121


#### Sim details ####
cycles = 20000 #number of cycles to run through
accept = 0
T = 35


#### particle details ####
particleOne = [1,0,0]
particleTwo = [0,1,0]
particleThree = [0,0,1]

rOne = distance(particleOne, particleTwo)
rTwo = distance(particleTwo, particleThree)
rThree = distance(particleThree, particleOne)
# r is distance between particles
    
energy = energyCalc(rOne)+energyCalc(rTwo)+energyCalc(rThree)


energyTotal = energy

accRatio = 0 

avg = 0

# loop that 
for i in range(cycles):
    
    #place holder for position in case system is rejected
    posPlaceOne = particleOne
    posPlaceTwo = particleTwo
    posPlaceThree = particleThree
    
    # calculates energy before move
    # for first loop this is the starting energy (1)
    energyOld = energy
    
    # pick particle to move        
       
    particleOne = move(maxDis, particleOne)
    
    rOne = distance(particleOne, particleTwo)
    rTwo = distance(particleTwo, particleThree)
    rThree = distance(particleThree, particleOne)
    # r is distance between particles
    
    energy = energyCalc(rOne)+energyCalc(rTwo)+energyCalc(rThree)
    
    # calculates new energy and finds dE = Old E - New E
    #dE = deltaE(energy,r)
    
    dE = energy - energyOld
        
    if dE > 0:
        w = math.exp(-(dE/T))
        print "W: ", w
        #get random # (0,1)
        
        if random.random < w: 
            print("Accepted up!")
            accept = accept + 1
            #add energy and calculate
            energyTotal = energy + energyTotal
            avg = float(energyTotal)/accept
        else:
            #print "reject"
            # keeps old energy
            energy = energyOld
            # keeps old location
            particleOne = posPlaceOne
            particleTwo = posPlaceTwo
            particleThree = posPlaceThree
    
    #accept if change in energy is negative/same
    if dE <= 0:
        print("Down!")
        accept = accept + 1
        energyTotal = energy + energyTotal
        avg = float(energyTotal)/accept
    
    #calculate avg energy
    
    
    
    accRatio = float(accept)/(i+1)
    
    print "AVG Eng: ", avg
    print "RATIO: ", accRatio
    
    

    
    
    
        
    
    
    
