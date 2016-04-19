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
            
# ExtDim_1 initial particle distance list code v2:

for i in partList:
            l = range(0, numPart)
            l = l[:partList.index(i)] + l[partList.index(i)+1:]
            #print("L: ", l)
            for j in l:
                initDist[str(i.num) + " and " + str(partList[j].num)] = distance4(i.pos, partList[j].pos)
                #print("Distance between ", partList.index(i)+1, "and ", j+1)
                #print(initDist[str(i.num) + " and " + str(partList[j].num)])
# ExteDim_2 moving particles perpendicular to gradient of energy        
for m in partList:
            pV = list(perpVect(step, m.pos))
            for s in range(4):
                m.nPos[s] = m.pos[s] + pV[s]
            for n in xrange(m.num+1, numPart+1):
                currDist[str(m.num) + " and " + str(n)] = distance4(m.nPos, partList[n-1].tempPos)
            m.tempPos = list(m.nPos)