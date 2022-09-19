from cache import Cache


class Cpu:

    def __init__(self) :
       self.cache=Cache()

    def writeCache(self, block,dir, data, state):
        pass

    def readCache(self, dir, data):
        pass

    def changeBlockState(self, state, block):
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
            if (x[1]==bin(dir)):
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
        cacheNum=1
        blockNum=1
        for x in caches:
            for y in x: #y = blocks
                if (y[1]==bin(dir)):
                    return[cacheNum,blockNum,y[0], dir]
                blockNum=blockNum+1
            cacheNum=cacheNum+1
        return False