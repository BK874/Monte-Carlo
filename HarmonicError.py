# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:17:19 2016

@author: brian
"""

import HarmonicMetropolis_4 as HM


def ErrorMargin(testNum):
    testCount = 0
    
    errors = []
    
    while testCount < testNum:
        error = abs(HM.expResult - HM.Metropolis(10000))
        errors.append(error)
        testCount += 1

    errTotal = 0
    
    for err in errors:
        errTotal += err
        
    avgErr = errTotal/testNum
    
    return avgErr
    
print("The average error was: ", ErrorMargin(10000))

# When starting at 0, T = 400, step size = 11.5 ** -9
# Average error of 10,000 trials with 10,000 steps: 
# 6.967460439833894e-23. Range:
# 2.691622995601661e-21 - 2.830972204398339e-21

# When starting at 0, T = 400, step size = 10
# and treating kT as 1 (beta = 1.0, multiply result by kT)
# Average error of 10,000 trials with 10,000 steps:
# 0.5000185820103494

# When starting at 0, T = 11.5 ** =9 with auto adjustments
# of +/- 0.05 to 11.5 when the acceptance rate fell below 47% 
# or above 53% the average error of 10,000 trials with 10,000
# steps: 1.0363384877414086e-22. Range:
# 2.657663751225859e-21 - 2.864931448774141e-21