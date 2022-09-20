from msilib.schema import Condition
from re import search
from cpu import Cpu


class Controller:

  def __init__(self):
    self.cpu = Cpu()
      
  def mesiRead(self, inst, cachesArray):
    dir=inst[2]
    searchResult=self.cpu.searchInCache(dir)
    #Mi cache tiene la dirección y el estado no es invalido
    if ((searchResult!=False) & (searchResult[1]!="I")):
      self.cpu.readCache()
    foreignSearch=self.cpu.searchInForeingCaches(cachesArray,dir)
    #Otra cache tiene la dirección
    if (foreignSearch!=False):
      myBlockToDo=["WRITE","S", ""]
      #Posibles estados de los bloques a leer
      match foreignSearch[2]:
        case "M": foreingBlockToDo=["READ","S", "WB"]; return [myBlockToDo,foreignSearch,foreingBlockToDo]
        case "E": foreingBlockToDo=["READ","S",""]; return [myBlockToDo,foreignSearch,foreingBlockToDo]
        case "S": foreingBlockToDo=["READ","S",""]; return [myBlockToDo,foreignSearch,foreingBlockToDo]

    #Nadie lo tiene y voy a leer de memoria
    else:
        myBlockToDo=["WRITE","S", "WB"]
        return [myBlockToDo, searchResult, [""]]

  
  def mesiWrite(self, inst, cachesArray):
    dir=inst[2]
    searchResult=self.cpu.searchInCache(dir)
    foreignSearch=self.cpu.searchInForeingCaches(cachesArray,dir)
    if (searchResult!=False):
      myBlockToDo=["WRITE","M",inst[3], ""]
      foreingBlockToDo=["","I", "checkWB"]
      #Cuando el bloque la dirección la tenemos nosotros y alguien mas
      if(foreignSearch!=False):
        return [myBlockToDo,foreignSearch,foreingBlockToDo]#Aqui debe checkear si debe hacer WB(en caso de que este en M)
      #Cuando solo nosotros tenemos la dirección
      else:
        self.cpu.writeCache(searchResult[1],dir,inst[3],"M")
        return "Ready"
    #Cuando solo está en memoria
    else:
      myBlockToDo=["","", inst[3], "WB"]
      return[myBlockToDo,searchResult,["","",""]]

      
      




  def MESI(self, inst , cachesArray):
    action=inst[1]
    dir=inst[2]
    if(action == "READ"):
      result=self.mesiRead(inst, cachesArray)
      return result

    if(action == "WRITE"):
      result=self.mesiWrite(inst,cachesArray)
      return result

          
        
        

