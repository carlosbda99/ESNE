#!/usr/bin/python3

import classes_proj_2bim
import os

listBand=[]
listDelay=[]
listJitter=[]
listLoss=[]
best=[]

obj=classes_proj_2bim.APINFO(None,None,None,None)

obj.getDATA(listBand,listDelay,listJitter,listLoss)

os.system('clear')
for x in range (6):
    print('AP_%d----------------------------------------------------------'%(x+1))
    print('Band: %07.3f\tDelay: %07.3f\tJitter: %07.3f\tLoss: %07.3f\n'%(listBand[x],listDelay[x],listJitter[x],listLoss[x]))

obj.setNorm(listBand,listDelay,listJitter,listLoss)

obj.setResult(best)
