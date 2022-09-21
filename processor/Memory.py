from block import Block

class Memory:
    flag=False

    def __init__(self) -> None:
        self.block1=Block(1)
        self.block2=Block(2)
        self.block3=Block(3)
        self.block4=Block(4)
        self.block5=Block(5)
        self.block6=Block(6)
        self.block7=Block(7)
        self.block8=Block(8)
    


    def findInMem(self,dir):
        blocks=[self.block1, self.block2, self.block3, self.block4, self.block5, self.block6, self.block7, self.block8]
        emptyBlock=0
        counter=0
        for x in blocks:
            if(x.dir==bin(0) & counter==0):
                emptyBlock=x.id
                counter=1
            if (x.dir==dir):
                return [[x.id, x.data],emptyBlock]
        if(emptyBlock!=0):
            return ["",emptyBlock]
        return False


    def writeMemory(self, dir, data):
        findBlock=self.findInMem(dir)
        if (findBlock!=False & findBlock[0]!=""):
            match findBlock[0]:
                case 1: self.block1.data=data
                case 2: self.block2.data=data
                case 3: self.block3.data=data
                case 4: self.block4.data=data
                case 5: self.block5.data=data
                case 6: self.block6.data=data
                case 7: self.block7.data=data
                case 8: self.block8.data=data  
         
        if (findBlock!=False & findBlock[0]==""):
            match findBlock[1]:
                case 1: self.block1.data=data; self.block1.dir=dir
                case 2: self.block2.data=data; self.block2.dir=dir
                case 3: self.block3.data=data; self.block3.dir=dir
                case 4: self.block4.data=data; self.block4.dir=dir
                case 5: self.block5.data=data; self.block5.dir=dir
                case 6: self.block6.data=data; self.block6.dir=dir
                case 7: self.block7.data=data; self.block7.dir=dir
                case 8: self.block8.data=data; self.block8.dir=dir

    def ReadMemory(self,dir):
        findBlock=self.findInMem(dir)
        if(findBlock!=False & findBlock[0]!=""):
            match findBlock[0]:
                case 1: return self.block1.data
                case 2: return self.block2.data
                case 3: return self.block3.data
                case 4: return self.block4.data
                case 5: return self.block5.data
                case 6: return self.block6.data
                case 7: return self.block7.data
                case 8: return self.block8.data 
        else:
            print("Address is not in memory")
                       
