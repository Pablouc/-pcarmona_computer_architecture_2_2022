from dis import Instruction
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
        print(currentCache)
        currentCache=[]
    print("------------------------------------------------------")
    return cachesArray



def cutArray(cacheNum, cachesArray):
    del cachesArray[cacheNum-1]
    return cachesArray
 
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
            #Read from the foreign Cache and get the datA           BLOQUE DIR ESTADO
            data=foreignProcessor.Controller.cpu.readCache(foreignData[1], foreignData[3], foreignToDo[1])[3]
            #Execute the Write Back---------Here it is needed to block the bus
            mem.writeMemory(foreignData[3], data)
            #-------------------------------the bus is free
            #Executing WRITE
            ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],foreignData[3],data, myBlockToDo[1])

        if(mesiResult[0]==2):
            #Read from the foreign Cache and get the data
            data=foreignProcessor.Controller.cpu.readCache(foreignData[1], foreignData[3], foreignToDo[1])[3]
             #Executing WRITE
            ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],foreignData[3],data, myBlockToDo[1])

        if(mesiResult[0]==3):
            #Read from memory---------Here it is needed to block the bus
            data= mem.readMemory(mesiResult[2])
            print("mesiiiiiu")
            print(mesiResult[2])
            #------------------------The bus is free
             #Executing WRITE
            ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],mesiResult[2],data,myBlockToDo[1])
        
        if(mesiResult[0]==4):
             #Executing WRITE
             ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],myBlockToDo[3], myBlockToDo[4],myBlockToDo[1])
             #Invalida ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],mesiResult[2],data,myBlockToDo[1])
             #Lista de caches con la direccion
             foreignCaches=foreignData
             #Loop para invalidar y checkear WB 
             for x in foreignCaches:

                foreignProcessor= getProcessor(x[0])
                match x[2]:
                    case "E": foreignProcessor.Controller.cpu.changeBlockState(foreignToDo[1], x[1])#Invalidar dato
                    case "S": foreignProcessor.Controller.cpu.changeBlockState(foreignToDo[1], x[1])#Invalidar dato
                    case "M": 
                        #Invalida Dato
                        foreignProcessor.Controller.cpu.changeBlockState(foreignToDo[1], x[1]); 
                        #Execute the Write Back---------Here it is needed to block the bus
                        mem.writeMemory(myBlockToDo[3],foreignProcessor.Controller.cpu.readCache(x[1],x[3],foreignToDo[1])[3])
                        #-------------------------------the bus is free
        if(mesiResult[0]==5):
            #Execute the Write Back---------Here it is needed to block the bus
            mem.writeMemory(myBlockToDo[3],myBlockToDo[4])
            #-------------------------------the bus is free
            #Executing WRITE
            ownProcessor.Controller.cpu.writeCache(myBlockToDo[2],myBlockToDo[3], myBlockToDo[4],myBlockToDo[1])
                         


def runProcessor(instruction):
    #instruction=generateInst()

    processor= getProcessor(instruction[0])

    cachesArray=getCachesArray()
    cachesArray=cutArray(instruction[0],cachesArray)
    mesiResult=processor.Controller.MESI(instruction,cachesArray)
    mesiFollowUp(instruction[0], mesiResult)
    print("Cache memory")
    getCachesArray()
    #print("Memory")
    mem.printMem()


instruction1=[1,"WRITE",bin(3), hex(50)]
instruction2=[4,"WRITE",bin(2), hex(20)]
instruction3=[3,"WRITE",bin(3), hex(10)]
instruction4=[1,"READ",bin(3)]
instruction5=[2,"READ",bin(2)]
instruction6=[2,"READ",bin(3)]
instruction7=[2,"WRITE",bin(4), hex(15)]
instruction8=[2,"WRITE",bin(5), hex(25)]
instruction9=[2,"WRITE",bin(6), hex(35)]
instruction10=[3,"READ",bin(5)]
runProcessor(instruction1)
runProcessor(instruction2)
runProcessor(instruction3)
runProcessor(instruction4)
runProcessor(instruction5)
runProcessor(instruction6)
runProcessor(instruction7)
runProcessor(instruction8)
runProcessor(instruction9)
runProcessor(instruction10)
