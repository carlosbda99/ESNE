#!/usr/bin/python3
#Randomizando os arquivos
import random

def randomB():
    a=('%.3f'%random.uniform(5,51))
    return str(a)+'\n'

def randomD():
    a=('%.3f'%random.uniform(10,150))
    return str(a)+'\n'

def randomJ():
    a=('%.3f'%random.uniform(20,250))
    return str(a)+'\n'

def randomL():
    a=('%.3f'%random.uniform(0,3))
    return str(a)

def randomDATA(i):
    if i==0:
        return randomB()
    elif i==1:
        return randomD()
    elif i==2:
        return randomJ()
    else:
        return randomL()

for x in range (6):
    arq=open('AP_%d.txt'%x,'w')
    for i in range (4):
        arq.write(randomDATA(i))
    arq.close()

'''arq=open('AP_%d.txt'%x,'r')
linhas=[]
for linha in arq:
    linhas.append(float(linha))
print(linhas)
linhas[0]=randomB()
linhas[1]=randomD()
linhas[2]=randomJ()
linhas[3]=randomL()
arq=open('AP_%d.txt'%x,'w')
print(linhas)
arq.close()'''
