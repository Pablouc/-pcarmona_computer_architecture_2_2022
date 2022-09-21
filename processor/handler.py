from Processor import Processor
from instructionGenerator import *

p1=Processor(1)
p2=Processor(2)
p3=Processor(3)
p4=Processor(4)

newInstruction = generateInst()
def getCachesArray():
    processors=[p1,p2,p3,p4]
    cachesArray=[]
    currentCache=[]
    for x in processors: 
        for y in range(1,5):
            match y:
                case 1: block = x.Controller.cpu.cache.block1
                case 2: block = x.Controller.cpu.cache.block2
                case 3: block = x.Controller.cpu.cache.block3
                case 4: block = x.Controller.cpu.cache.block4
            state= block.state
            dir= block.dir
            data= block.data
            blockArray=[state, dir, data]
            currentCache.append(blockArray)
        cachesArray.append(currentCache)
        #print(currentCache)
        currentCache=[]
    return cachesArray

def cutArray(cachenum, cachesArray):
    del cachesArray[cachenum-1]
    del cachesArray[cachenum-1]
    #cacheArray.pop(cachenum)
    counter=0
    for x in cachesArray:
        print(cachesArray[counter])
        counter=counter+1
    return cachesArray

cutArray(1, getCachesArray())  

            
getCachesArray()

def runProcessor():

    if(newInstruction[0]==1):
        p1.Controller.MESI()

    

