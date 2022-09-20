
from Controller import Controller

class Processor:
  #Specific order for caches
  #from lowest to highest
  #Ex.If this is the processor 1: 
  #cachesArray=[cache2,cache3,cache4]
  cachesArray=[]

  def __init__(self, id):
    self.id=id
    self.Controller = Controller()
    
    
  def getCachesData(self, cache1, cache2, cache3):
    self.cachesArray=[cache1,cache2,cache3]


  def control(self):
    self.controller.MESI()


  