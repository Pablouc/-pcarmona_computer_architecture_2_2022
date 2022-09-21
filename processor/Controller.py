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
    #Es cuando estoy en M-S-E
    #Tengo que indicarle que lea el dato y le mantenga el estado
    if ((searchResult!=False) & (searchResult[1]!="I")):
      self.cpu.readCache(searchResult[0],searchResult[2], searchResult[1])
    foreignSearch=self.cpu.searchInForeingCaches(cachesArray,dir)

    #Otra cache tiene la dirección y estamos en estado Invalido
    if((searchResult!=False) & (searchResult[1]=="I")):
      if (foreignSearch!=False):
        myBlockToDo=["WRITE","S",searchResult[0], ""]
        #Posibles estados de los bloques a leer
        match foreignSearch[2]:
          case "M": foreingBlockToDo=["READ","S", "WB"]; return [1,myBlockToDo,foreignSearch,foreingBlockToDo]
          case "E": foreingBlockToDo=["READ","S",""]; return [2,myBlockToDo,foreignSearch,foreingBlockToDo]
          case "S": foreingBlockToDo=["READ","S",""]; return [2,myBlockToDo,foreignSearch,foreingBlockToDo]

    #Nadie lo tiene y voy a leer de memoria
    #Implica que escribo un nuevo bloque de cache con estado E
    else:
        myBlockToDo=["WRITE","E","", "WB"]
        return [3,myBlockToDo, dir, [""]]

  
  def mesiWrite(self, inst, cachesArray):
    dir=inst[2]
    searchResult=self.cpu.searchInCache(dir)
    foreignSearch=self.cpu.searchInForeingCaches(cachesArray,dir)
    if (searchResult!=False):
      myBlockToDo=["WRITE","M",searchResult[0], ""]
      foreingBlockToDo=["","I", ""]
      #Cuando la dirección la tenemos nosotros y alguien mas
      #Necesito una lista completa de todos los que tienen la direccion
      #y hacer un match por caso
      if(foreignSearch!=False):
        foreignCaches=self.cpu.listOfForeignCaches(cachesArray,dir)
        for x in foreignCaches:
          for y in x:
            match y[2]:
              case "E": return [4,myBlockToDo,x,foreingBlockToDo]#Solo me manda a escribir e invalidar al otro
              case "S": return [4,myBlockToDo,x,foreingBlockToDo]#Solo me manda a escribir e invalidar al otro
              case "M": return [5,myBlockToDo,x, ["","I","WB"]]#Solo me manda a escribir e invalidar al otro (a ese otro le toca WB)
      #Cuando solo nosotros tenemos la dirección
      else:
        self.cpu.writeCache(searchResult[1],dir,inst[3],"M")
        return ["Ready"]
    #Cuando solo está en memoria
    #Toca escribirlo en mem y escribirlo en cache
    #Quedamos en estado E
    else:
      myBlockToDo=["WRITE","E", "", "WB"]
      return[6,myBlockToDo,dir, [""]]

      
      




  def MESI(self, inst , cachesArray):
    action=inst[1]
    dir=inst[2]
    if(action == "READ"):
      result=self.mesiRead(inst, cachesArray)
      return result

    if(action == "WRITE"):
      result=self.mesiWrite(inst,cachesArray)
      return result

          
        
        

