from msilib.schema import Condition
from re import search
from cpu import Cpu


class Controller:

  def __init__(self):
    self.cpu = Cpu()
      
  def mesiRead(self, inst, cachesArray):
    dir=inst[2]
    searchResult=self.cpu.searchInCache(dir)
    #Mi cache tiene la dirección y el estado no es Invalido
    #Es cuando estoy en M-S-E
    #Tengo que indicarle que lea el dato y le mantenga el estado
    if (searchResult!=False):
      if (searchResult[1]!="I"):
        self.cpu.readCache(searchResult[0],searchResult[2], searchResult[1])
        return ["Ready"]
    foreignSearch=self.cpu.searchInForeingCaches(cachesArray,dir)

    #Otra cache tiene la dirección y estamos en estado Invalido
    #if(searchResult!=False):
    #  if(searchResult[1]=="I"):
    if (foreignSearch!=False):
      if(searchResult!=False):
        myBlockToDo=["WRITE","S",searchResult[0], ""]
      #Generar read miss
      if(searchResult==False):
        self.cpu.cache.readMiss=True
        myBlockToDo=["WRITE","S","", ""]
      #Posibles estados de los bloques a leer
      match foreignSearch[2]:                         
        case "M": foreingBlockToDo=["READ","S", "WB"]; return [1,myBlockToDo,foreignSearch,foreingBlockToDo]; print("******1****")
        case "E": foreingBlockToDo=["READ","S",""]; return [2,myBlockToDo,foreignSearch,foreingBlockToDo]; print("******2****")
        case "S": foreingBlockToDo=["READ","S",""]; return [2,myBlockToDo,foreignSearch,foreingBlockToDo]; print("******2****")

    #Nadie lo tiene y voy a leer de memoria
    #Implica que escribo un nuevo bloque de cache con estado E
    #Genero read miss
    else:
        self.cpu.cache.readMiss=True
        myBlockToDo=["WRITE","E","", "WB"]
        print("******3****")
        return [3,myBlockToDo, dir, [""]]

  
  def mesiWrite(self, inst, cachesArray):
    dir=inst[2]
    data=inst[3]
    searchResult=self.cpu.searchInCache(dir)
    foreignSearch=self.cpu.searchInForeingCaches(cachesArray,dir)
    if(searchResult==False):
      #Aqui hay un write miss
      #Lo  quiero escribir, pero no lo tengo
      self.cpu.cache.writeMiss=True
      if(type(foreignSearch)==list):
        myBlockToDo=["WRITE","M","", dir, data]
        foreingBlockToDo=["","I", ""]
        foreignCaches=self.cpu.listOfForeignCaches(cachesArray,dir)
        print("******4.1***********")
        return [4,myBlockToDo,foreignCaches,foreingBlockToDo]


    if (searchResult!=False):

      myBlockToDo=["WRITE","M",searchResult[0], dir, data]
      foreingBlockToDo=["","I", ""]

      #Cuando la dirección la tenemos nosotros y alguien mas
      #Necesito una lista completa de todos los que tienen la direccion
      #y hacer un match por caso
      if(foreignSearch!=False):
        foreignCaches=self.cpu.listOfForeignCaches(cachesArray,dir)
        print("******4***********")
        return [4,myBlockToDo,foreignCaches,foreingBlockToDo]

      #Cuando solo nosotros tenemos la dirección
      if(foreignSearch==False):
        print("data:"+ data)
        self.cpu.writeCache(searchResult[0],dir,data,"M")
        print("******WRITE READY***********")
        return ["Ready"]
        
    #Cuando nadie lo tiene
    #Aqui hay un write miss, estoy en invalido y paso a modificado
    #Nadie más lo tiene
    else:
      self.cpu.cache.writeMiss=True
      myBlockToDo=["WRITE","M", "", dir, data]
      print("******5***********")
      self.cpu.writeCache("",dir,data,"M")
      #return[5,myBlockToDo,dir, [""]]

      
      




  def MESI(self, inst , cachesArray):
    action=inst[1]
    dir=inst[2]
    if(action == "READ"):
      result=self.mesiRead(inst, cachesArray)
      return result

    if(action == "WRITE"):
      result=self.mesiWrite(inst,cachesArray)
      return result

          
        
        

