
from math import e
from random import choices


def distribution(x,u):
    prob=0
    fact=1

    #Calculate factorial of x
    for i in range(1,x+1):
        fact = fact * i

    #Poisson distribution
    prob=(e**(-u)*u**x)/(fact)
    return prob

def setProbabilities():
    pNumber=[]
    operation=[]
    dir=[]
    data=[]

    #Distribution for processor number
    for x in range(1,5):
        prob=distribution(x,2)
        pNumber.append(prob)

    #Distribution for operation
    for x in range(1,4):
        prob=distribution(x,2)
        operation.append(prob)

    #Distribution for direction
    for x in range(0,8):
        prob=distribution(x,4)
        dir.append(prob)

    #Distribution for data
    for x in range(0,150):
        prob=distribution(x,30)
        data.append(prob)
    
    return [pNumber,operation,dir,data]

def generateInst():
    processor=0
    op=0
    dir=0
    data=0
    inst=[]
    probabilities= setProbabilities()

    #con el metodo choices se elige un elemento de la primera lista dada una probabilidad
    #o sea pesos, dados en la segunda lista
    processor = choices([1,2,3,4],probabilities[0])[0]
    op=choices([1,2,3],probabilities[1])[0]
    dir=choices([0,1,2,3,4,5,6,7],probabilities[2])[0]
    
    dataList=[]
    #creación de la lista de posibles datos
    for x in range(0,150):
        dataList.append(x)
    
    data=choices(dataList,probabilities[3])[0]

    #Instrucción generada
    inst=[processor, op, dir, data]
    print(inst)
    inst=changeInstSyntax(inst)
    print(inst)

    return inst

def changeInstSyntax( instruction):
    newInst=[]
    newOp=""
    match instruction[1]:
        case 1:
            newOp="CALC"
        case 2:
            newOp="WRITE"
        case 3:
            newOp="READ"


    newInst=[instruction[0], newOp, bin(instruction[2]), hex(instruction[3])]
    return newInst

