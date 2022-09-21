from block import Block

class Cache:

    writeMiss=False
    ReadMiss=False
    
    def __init__(self) -> None:
        self.block1=Block(1)
        self.block2=Block(2)
        self.block3=Block(3)
        self.block4=Block(4)

    #Function to generate an array of the information of all the blocks
    #Return: Each block has the following structure B1=[state,dir,data]
    # and the function return an array like this one [B1,B2,B3,B4]
    def generateBlocksArray(self):
        blocksArray=[]
        for x in range(1,5):
            match x:
                case 1: blockNumber=self.block1
                case 2: blockNumber=self.block2
                case 3: blockNumber=self.block3
                case 4: blockNumber=self.block4
            state=blockNumber.state
            dir=blockNumber.dir
            data=blockNumber.data
            block=[state, dir, data]
            blocksArray.append(block)
        return blocksArray