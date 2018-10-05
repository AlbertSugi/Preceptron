# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:23:57 2018

@author: Albert
"""
from pylab import rand,plot,norm
class Perceptron:
    def __init__(self):
        self.weight = rand(2)*2-1
        self.LearnRate = 0.1
    
    def output(self,x):
        #wTxT Calculation
        y = x[0]*self.weight[0]+x[1]*self.weight[1]
        if y >=0:
            return 1
        else:
            return -1
    
    def updateweights(self,x,error):
        #W(t+1) = w(t) + learning rate*(true label - predicted label)*x
        #error = (true label - predicted label)
        self.weight[0]= self.weight[0]+self.LearnRate*error*x[0]
        self.weight[1]=self.weight[1]+self.LearnRate*error*x[1]
    
    def train(self,data,epoch):
        learn = False
        numepoch = 0
        while not learn:
            totalError = 0.0
            for c in data:
                checkweight=self.output(c)
                if c[2] != checkweight:
                    predicterror = c[2]-checkweight
                    self.updateweights(c,predicterror)
                    totalError = totalError + predicterror
                numepoch +=1
                
                if totalError ==0.0 or numepoch >=epoch:
    
                    learn = True
            print('iterations =', epoch,"GlobalError =",totalError)
            

def SepGenerateData(n):
    xa = (rand(n)*2-1)/2-0.5
    ya = (rand(n)*2-1)/2+0.5
    xb = (rand(n)*2-1)/2+0.5
    yb = (rand(n)*2-1)/2-0.5
    Data = []
    for i in range(len(xb)):
        Data.append([xa[i],ya[i],1])
        Data.append([xb[i],yb[i],-1])
    return Data

def UnSepGenerateData(n):
    xa = (rand(n)*2-1)/2-0.5
    ya = (rand(n)*2-1)/2+0.5
    xb = (rand(n)*2-1)/2-0.5
    yb = (rand(n)*2-1)/2+0.5
  
    Data = []
    for i in range(len(xa)):
        Data.append([xa[i],ya[i],1])
        Data.append([xb[i],yb[i],-1])
    return Data

def plotGraph(Dataset,train,test,epoch):
    traindata= Dataset(train)
    perceptron = Perceptron()
    perceptron.train(traindata,200)
    testdata = Dataset(test)
    for x in testdata:
        if x[2] ==1:
            plot(x[0],x[1],'ob')
        if x[2]==-1:
            plot(x[0],x[1],'or')
        
    n = norm(perceptron.weight)
    ww = perceptron.weight/n
    ww1=[ww[1],-ww[0]]
    ww2 = [-ww[1],ww[0]]
    plot([ww1[0],ww2[0]],[ww1[1],ww2[1]],'--k')
    Error = 0
    for x in testdata:
        prediction = perceptron.output(x)
        if prediction != x[2]:
            Error = Error +1
    print("Accuracy =" ,1.0- (Error/test))
    
    
plotGraph(SepGenerateData,100,30,200)   
#plotGraph(UnSepGenerateData,100,30,200)
    
    
    
    
    
    
    
    
