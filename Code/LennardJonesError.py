# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:44:03 2016

@author: brian
"""

import LennardJones_1 as LJ


def ErrorMargin(testNum):
    testCount = 0
    
    errors = []
    
    while testCount < testNum:
        error = (LJ.Metropolis(10000))
        errors.append(error)
        testCount += 1

    errTotal = 0
    
    for err in errors:
        errTotal += err
        
    avgErr = errTotal/testNum
    
    return avgErr

margin = ErrorMargin(10000)

print("The total average energy was: ", margin)
#print("This gives it a range of ", LJ.expResult - margin, " to ", 
#      LJ.expResult + margin)

# When starting at 1, 0 0; 0, 1, 0; and 0, 0 1; T = 20, step size = 11.5 ** -9
# Average energy over 1000 trials with 100,000 steps: 
# 107,721,762.30714966

# When starting at 1, 0 0; 0, 1, 0; and 0, 0 1; T = 20, step size = 11.5 ** -9
# Average energy over 10,000 trials with 10,000 steps: 
# 107,723,134.25485165


# When starting at 1, 0 0; 0, 1, 0; and 0, 0 1; T = 20, step size = 11.5 ** -9
# Average energy over 100,000 trials with 100,000 steps: 
# 
