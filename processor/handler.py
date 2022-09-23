import concurrent.futures
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
                         


def runProcessor(mode,instruction, coreNum):
    existInMem=False
    if(mode==1):
        #Making sure not to read something that does not exist
        while(existInMem==False):
            instruction=generateInst()
            if(instruction[1]=="READ"):
                if(mem.findInMem(instruction[2])!=False):
                    existInMem=True
            else: existInMem=True
            
    processor= getProcessor(coreNum)
    cachesArray=getCachesArray()
    cachesArray=cutArray(coreNum,cachesArray)
    mesiResult=processor.Controller.MESI(instruction,cachesArray)
    mesiFollowUp(coreNum, mesiResult)
    print("Cache memory")
    getCachesArray()
    #print("Memory")
    mem.printMem()



#--------------------------------------Main Program----------------------------------

#Global Variables
next_Step=False
continuous=False
step_By_Step=True
pause=False
new_Inst=False
entry_Inst=[]



def run_All(index):
    print("runing processor")
    print(index)
    while True:
        if(continuous==True):
            while(pause!=True):
                runProcessor(1,[],index)
            if(new_Inst==True):
                runProcessor(2,entry_Inst, index)
        
        if(step_By_Step==True):
            runProcessor(1,[],index)
            if(next_Step==True):
                runProcessor(1,[],index)
                next_Step=False
            if(new_Inst==True):
                runProcessor(2,entry_Inst, index)



            


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for index in range(1,5):
        executor.submit(run_All,index)
    # Another thread is required for the interface




