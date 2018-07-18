#!/usr/bin/python3

class APINFO(object):
    def __init__ (self, band, delay, jitter, loss):
        self.band=band
        self.delay=delay
        self.jitter=jitter
        self.loss=loss

    def getDATA(self,listB,listD,listJ,listL):
        for x in range (6):
            arq=open('AP_%d.txt'%x)
            self.band=float(arq.readline())
            self.delay=float(arq.readline())
            self.jitter=float(arq.readline())
            self.loss=float(arq.readline())
            listB.append(self.band)
            listD.append(self.delay)
            listJ.append(self.jitter)
            listL.append(self.loss)
            arq.close()

    def setNorm(self,listB,listD,listJ,listL):
        global listB1, listD1, listJ1, listL1
        listB1=[]
        listD1=[]
        listJ1=[]
        listL1=[]
        for i in range(6):
            listB1.append((listB[i]-min(listB))/(max(listB)-min(listB)))
            listD1.append((max(listD)-listD[i])/(max(listD)-min(listD)))
            listJ1.append((max(listJ)-listJ[i])/(max(listJ)-min(listJ)))
            listL1.append((max(listL)-listL[i])/(max(listL)-min(listL)))

    def setResult(self,best):
        for i in range (6):
            #pontos=(listB1[i]*4.0)+(listD1[i]*3.0)+(listJ1[i]*2.0)+(listL1[1]*1.0)???????
            pontos=(listB1[i]*4+listD1[i]*3+listJ1[i]*2+listL1[i]*1)
            best.append(pontos)
            if best[i]==max(best):
                melhorap=i+1
        print ('O melhor Acess Point é o: AP_',melhorap)
        for i in range (6):
            print ('Pontuaçao do AP_%d: %.3f'%(i+1,best[i]))
