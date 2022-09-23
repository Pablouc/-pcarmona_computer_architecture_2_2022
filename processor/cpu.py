from cache import Cache
import time


class Cpu:
    #Replacement policy: LIFO
    lastBlockChanged=0

    def __init__(self) :
       self.cache=Cache()
    #When block is empty it means that a replacement is required
    def writeCache(self, block, dir, data, stateToChange):
        time.sleep(2)
        cache=self.cache
        if(block==""):
            blockToWrite= self.checkBlockSpace()
            if(blockToWrite!=""):
                print("There is a free block") 
                blockToWrite.dir=dir 
                blockToWrite.state= stateToChange
                blockToWrite.data=data
                self.lastBlockChanged=blockToWrite.id
            if(blockToWrite==""):
                print("Applying replacement policy")
                print(self.lastBlockChanged)
                match self.lastBlockChanged:
                    case 1: cache.block1.dir=dir; cache.block1.state= stateToChange; cache.block1.data=data
                    case 2: cache.block2.dir=dir; cache.block2.state= stateToChange; cache.block2.data=data
                    case 3: cache.block3.dir=dir; cache.block3.state= stateToChange; cache.block3.data=data
                    case 4: cache.block4.dir=dir; cache.block4.state= stateToChange; cache.block4.data=data
        else:
            match block:
                case 1:  cache.block1.state= stateToChange; cache.block1.data=data; self.lastBlockChanged=1
                case 2:  cache.block2.state= stateToChange; cache.block2.data=data; self.lastBlockChanged=2
                case 3:  cache.block3.state= stateToChange; cache.block3.data=data; self.lastBlockChanged=3
                case 4:  cache.block4.state= stateToChange; cache.block4.data=data; self.lastBlockChanged=4

    def checkBlockSpace(self):
        if(self.cache.block1.dir==bin(0)):
            return self.cache.block1
        if(self.cache.block2.dir==bin(0)):
            return self.cache.block2
        if(self.cache.block3.dir==bin(0)):
            return self.cache.block3
        if(self.cache.block4.dir==bin(0)):
            return self.cache.block4
        else: return ""

    #Reads the cache
    #Receive the blocks number and the address
    # Returns [block's number, state, address, data]               
    def readCache(self, block, dir, state):
        time.sleep(2)
        cache=self.cache
        match block:
                case 1:  cache.block1.state=state; data=cache.block1.data
                case 2:  cache.block2.state=state; data=cache.block2.data 
                case 3:  cache.block3.state=state; data=cache.block3.data 
                case 4:  cache.block4.state=state; data=cache.block4.data
        return[block, state, dir, data]

    def changeBlockState(self, state, block):
        time.sleep(2)
        match block:
            case 1: self.cache.block1.state=state
            case 2: self.cache.block2.state=state
            case 3: self.cache.block3.state=state
            case 4: self.cache.block4.state=state
    
    #Function to search for a specific address in the processor's cache
    #Parameters: blocks is an array of the 4 memory blocks. Each block 
    # has the following structure B1=[state,dir,data], so blocks looks like this  [B1,B2,B3,B4]
    # dir is the address we are loocking for.
    #Return: [block's number, block's state, dir] or False
    def searchInCache(self, dir):
        blocks=self.cache.generateBlocksArray()
        counter=1
        for x in blocks:
            if (x[1]==dir):
                return [counter,x[0],dir]
            counter=counter+1
        return False
    
    
    #Function to search in the other caches for a specific address
    #Parameter: blocks has the following structure:
    #caches:[C1,C2,C3,C4] and each item looks like this
    #C1=[B1,B2,B3,B4] where each item is an array: B1[state,dir,data]
    #dir is the address we are loocking for.
    #Return: [cache's number, block's number, block's state, dir] or False
    def searchInForeingCaches(self, caches, dir):
        for x in caches:
            for y in x: #y = blocks
                #verifico que tenga la dirección que busco y que es estado no sea inválido
                if ((y[1]==dir) & (y[0]!="I")):
                    return[y[3],y[4],y[0], dir]
            
        return False
    
    #Same function than above, but it returns the full list of 
    #caches with the required address
    def listOfForeignCaches(self, caches, dir):
        foreignCaches=[]
        for x in caches:
            for y in x: #y = blocks
                #verifico que tenga la dirección que busco y que es estado no sea inválido
                if ((y[1]==dir) & (y[0]!="I")):
                    foreignCaches.append([y[3],y[4],y[0], dir])
        if(foreignCaches!=[]): return foreignCaches
        else: return False

#cpu=Cpu()
#cpu.searchInCache(bin(3))