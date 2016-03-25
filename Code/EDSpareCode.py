# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:40:31 2016

@author: brian
"""

#ExtDim_1 initial particle distane list code:

initDist = []

 for i in partList:
        l = range(0, len(partList))
        l = l[:partList.index(i)] + l[partList.index(i)+1:]
        print("L: ", l)
        for j in l:
            initDist.append(distance4(i.pos, partList[j].pos))
            print("Distance between ", partList.index(i), "and ",
            j)
            print(distance4(i.pos, partList[j].pos))