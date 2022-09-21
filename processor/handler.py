from functools import cache
from Processor import Processor
from instructionGenerator import *
from Memory import Memory

p1=Processor(1)
p2=Processor(2)
p3=Processor(3)
p4=Processor(4)
mem=Memory()

newInstruction = generateInst()
def getCachesArray():
    processors=[p1,p2,p3,p4]
    cachesArray=[]
    currentCache=[]
    cacheNum=1
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
            blockNum=block.id
            blockArray=[state, dir, data, cacheNum, blockNum]
            currentCache.append(blockArray)
        cachesArray.append(currentCache)
        cacheNum=cacheNum+1
        #print(currentCache)
        currentCache=[]
    return cachesArray



def cutArray(cacheNum, cachesArray):
    del cachesArray[cacheNum-1]
 
def getProcessor(processorNum):
    match processorNum:
        case 1: return p1
        case 2: return p2
        case 3: return p3
        case 4: return p4


def mesiFollowUp(ownProcessor, mesiResult):
    if (mesiResult[0]!="Ready"):
        myBlockToDo=mesiResult[1]
        foreignData=mesiResult[2]
        foreignToDo=mesiResult[3]
        ownProcessor=getProcessor(ownProcessor)
        foreignProcessor= getProcessor(mesiResult[2][0])
    
        if (mesiResult[0]==1):
            #Read from the foreign Cache and get the data
            data=foreignProcessor.Controller.cpu.readCache(foreignData[1], foreignData[3], foreignData[2])[3]
            #Execute the Write Back---------Here it is needed to block the bus
            mem.writeMemory(foreignData[3], data)
            #-----------the bus is free
            #Executing WRITE
            ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],foreignData[3],data, myBlockToDo[1])
            







def runProcessor():
    instruction=generateInst()

    processor= getProcessor(instruction[0])

    cachesArray=getCachesArray()
    cachesArray=cutArray(1,cachesArray)
    mesiResult=processor.Controller.MESI(instruction,cachesArray)
    mesiFollowUp(instruction[0], mesiResult)

