import tkinter as tk
import sys 
sys.path.insert(1, 'C:/Users/Pablo/Desktop/TEC/II Semestre 2022/Arqui II/Proyecto1/-pcarmona_computer_architecture_2_2022/processor')
import handler
import concurrent.futures




def sendInst(event):
    pass


            
def step_By_Step(event):
    pass


def pause(event):
    pass


def continuous(event):
    pass






#Functions

def generateGrid_Core1():
    for i in range(5):
        for j in range(4):
            gridFrame1 = tk.Frame(master=frame_Core1,relief=tk.RAISED,borderwidth=1)
            gridFrame1.grid(row=i, column=j, padx=5, pady=5)
            cacheBlock=handler.p1.Controller.cpu.cache
            match i:
                case 1: cacheBlock=cacheBlock.block1
                case 2: cacheBlock=cacheBlock.block2
                case 3: cacheBlock=cacheBlock.block3
                case 4: cacheBlock=cacheBlock.block4
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="Estado"
                        case 2: name="Dirección"
                        case 3: name="Dato"
                    label = tk.Label(master=gridFrame1, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(j==1):
                if(i>0):
                    label = tk.Label(master=gridFrame1, text=str(cacheBlock.state), width=10, height=2)
                    label.pack()
                    continue
            if(j==2):
                if(i>0):
                    label = tk.Label(master=gridFrame1, text=str(cacheBlock.dir), width=10, height=2)
                    label.pack()
                    continue
            if(j==3):
                if(i>0):
                    label = tk.Label(master=gridFrame1, text=str(cacheBlock.data), width=10, height=2)
                    label.pack()
                    continue

            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame1, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
            
            label = tk.Label(master=gridFrame1, text=f"0", width=8, height=2)
            label.pack()
    lbl_Core1_InstData.config(text=handler.p1.instruction)
    #frame_Core1.after(3000,generateGrid_Core1)
            
def generateGrid_Core2():
    for i in range(5):
        for j in range(4):
            gridFrame2 = tk.Frame(master=frame_Core2,relief=tk.RAISED,borderwidth=1)
            gridFrame2.grid(row=i, column=j, padx=5, pady=5)
            cacheBlock=handler.p2.Controller.cpu.cache
            match i:
                case 1: cacheBlock=cacheBlock.block1
                case 2: cacheBlock=cacheBlock.block2
                case 3: cacheBlock=cacheBlock.block3
                case 4: cacheBlock=cacheBlock.block4

            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="Estado"
                        case 2: name="Dirección"
                        case 3: name="Dato"
                    label = tk.Label(master=gridFrame2, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(j==1):
                if(i>0):
                    label = tk.Label(master=gridFrame2, text=str(cacheBlock.state), width=10, height=2)
                    label.pack()
                    continue
            if(j==2):
                if(i>0):
                    label = tk.Label(master=gridFrame2, text=str(cacheBlock.dir), width=10, height=2)
                    label.pack()
                    continue
            if(j==3):
                if(i>0):
                    label = tk.Label(master=gridFrame2, text=str(cacheBlock.data), width=10, height=2)
                    label.pack()
                    continue
            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame2, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
            
            label = tk.Label(master=gridFrame2, text=f"0", width=8, height=2)
            label.pack()
    lbl_Core2_InstData.config(text=handler.p2.instruction)
    #frame_Core2.after(3000,generateGrid_Core2)

def generateGrid_Core3():
    for i in range(5):
        for j in range(4):
            gridFrame3 = tk.Frame(master=frame_Core3,relief=tk.RAISED,borderwidth=1)
            gridFrame3.grid(row=i, column=j, padx=5, pady=5)
            cacheBlock=handler.p3.Controller.cpu.cache
            match i:
                case 1: cacheBlock=cacheBlock.block1
                case 2: cacheBlock=cacheBlock.block2
                case 3: cacheBlock=cacheBlock.block3
                case 4: cacheBlock=cacheBlock.block4
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="Estado"
                        case 2: name="Dirección"
                        case 3: name="Dato"
                    label = tk.Label(master=gridFrame3, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(j==1):
                if(i>0):
                    label = tk.Label(master=gridFrame3, text=str(cacheBlock.state), width=10, height=2)
                    label.pack()
                    continue
            if(j==2):
                if(i>0):
                    label = tk.Label(master=gridFrame3, text=str(cacheBlock.dir), width=10, height=2)
                    label.pack()
                    continue
            if(j==3):
                if(i>0):
                    label = tk.Label(master=gridFrame3, text=str(cacheBlock.data), width=10, height=2)
                    label.pack()
                    continue

            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame3, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
            
            label = tk.Label(master=gridFrame3, text=f"0", width=8, height=2)
            label.pack()

    lbl_Core3_InstData.config(text=handler.p3.instruction)
    #frame_Core3.after(3000,generateGrid_Core3)

def generateGrid_Core4():
    for i in range(5):
        for j in range(4):
            gridFrame4 = tk.Frame(master=frame_Core4,relief=tk.RAISED,borderwidth=1)
            gridFrame4.grid(row=i, column=j, padx=5, pady=5)
            cacheBlock=handler.p4.Controller.cpu.cache
            match i:
                case 1: cacheBlock=cacheBlock.block1
                case 2: cacheBlock=cacheBlock.block2
                case 3: cacheBlock=cacheBlock.block3
                case 4: cacheBlock=cacheBlock.block4
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="Estado"
                        case 2: name="Dirección"
                        case 3: name="Dato"
                    label = tk.Label(master=gridFrame4, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(j==1):
                if(i>0):
                    label = tk.Label(master=gridFrame4, text=str(cacheBlock.state), width=10, height=2)
                    label.pack()
                    continue
            if(j==2):
                if(i>0):
                    label = tk.Label(master=gridFrame4, text=str(cacheBlock.dir), width=10, height=2)
                    label.pack()
                    continue
            if(j==3):
                if(i>0):
                    label = tk.Label(master=gridFrame4, text=str(cacheBlock.data), width=10, height=2)
                    label.pack()
                    continue

            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame4, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
            
            label = tk.Label(master=gridFrame4, text=f"0", width=8, height=2)
            label.pack()
    lbl_Core4_InstData.config(text=handler.p4.instruction)
    #frame_Core4.after(3000,generateGrid_Core4)

def generateGrid_Mem():
    for i in range(9):
        for j in range(3):
            gridFrameMem = tk.Frame(master=frame_Mem,relief=tk.RAISED,borderwidth=1)
            gridFrameMem.grid(row=i, column=j, padx=5, pady=5)
            memBlock=handler.mem
            match i:
                case 1: memBlock = memBlock.block1
                case 2: memBlock = memBlock.block2
                case 3: memBlock = memBlock.block3
                case 4: memBlock = memBlock.block4
                case 5: memBlock = memBlock.block5
                case 6: memBlock = memBlock.block6
                case 7: memBlock = memBlock.block7
                case 8: memBlock = memBlock.block8

            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="Dirección"
                        case 2: name="Dato"
                    label = tk.Label(master=gridFrameMem, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(j==1):
                if(i>0):
                    label = tk.Label(master=gridFrameMem, text=str(memBlock.dir), width=10, height=2)
                    label.pack()
                    continue
            if(j==2):
                if(i>0):
                    label = tk.Label(master=gridFrameMem, text=str(memBlock.data), width=10, height=2)
                    label.pack()
                    continue

            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrameMem, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
            
            label = tk.Label(master=gridFrameMem, text=f"0", width=8, height=2)
            label.pack()  
    #frame_Mem.after(3000,generateGrid_Mem)    

def next_Step(event):
    #Threads 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(1,5):
            executor.submit(handler.runProcessor,1,[], index)
    generateGrid_Core1()
    generateGrid_Core2()
    generateGrid_Core3()
    generateGrid_Core4()
    generateGrid_Mem()


window =tk.Tk()
window.geometry("1500x900")


#Top frame with the menu
frame_Menu=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

#Creating 4 frames, one for each core
frame_Core1=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

frame_Core2=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

frame_Core3=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

frame_Core4=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

frame_Mem=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

#Creating the menu
btn_Continuous=tk.Button(master=frame_Menu,text="Continuo", font=(25))
btn_Continuous.pack(side=tk.LEFT,expand=True)
btn_Continuous.bind('<Button-1>', continuous)

btn_Pause=tk.Button(master=frame_Menu, text="Pausa",  font=(25))
btn_Pause.pack( side=tk.LEFT,expand=True)
btn_Pause.bind('<Button-1>', pause)

btn_Step_by_Step=tk.Button(master=frame_Menu, text="Paso a paso", font=(25))
btn_Step_by_Step.pack(side=tk.LEFT,expand=True)
btn_Step_by_Step.bind('<Button-1>', step_By_Step)

btn_Next_Step=tk.Button(master=frame_Menu, text="Siguiente", font=(25))
btn_Next_Step.pack(side=tk.LEFT,expand=True)
btn_Next_Step.bind('<Button-1>', next_Step)

lbl_Inst = tk.Label(master=frame_Menu, text="Instrucción", font=(25))
lbl_Inst.pack( side=tk.LEFT,expand=True)

input_Inst = tk.Entry(master=frame_Menu, font=(25))
input_Inst.pack( side=tk.LEFT,expand=True)
#To get input_Inst data
# entry.get()

btn_sendInst=tk.Button(master=frame_Menu,text="Enviar", font=(25)) 
btn_sendInst.pack(side=tk.LEFT,expand=True)
btn_sendInst.bind('<Button-1>', sendInst)

#Processor 1 layout

lbl_Core1 = tk.Label(master=frame_Core1, text="CORE 1", font="bold")
lbl_Core1.grid(row=5, column=0)
lbl_Core1.config(bg="yellow")

lbl_Core1_Wmiss = tk.Label(master=frame_Core1, relief=tk.RAISED,text="write miss" )
lbl_Core1_Wmiss.grid(row=5, column=1)

lbl_Core1_Rmiss = tk.Label(master=frame_Core1,relief=tk.RAISED, text="read miss")
lbl_Core1_Rmiss.grid(row=5, column=2)

lbl_Core1_Inst = tk.Label(master=frame_Core1,relief=tk.RAISED, text="Instrucción", font="bold")
lbl_Core1_Inst.grid(row=6, column=0)

lbl_Core1_InstData = tk.Label(master=frame_Core1,relief=tk.RAISED, text=handler.p1.instruction, font="bold")
lbl_Core1_InstData.grid(row=6, column=1)

generateGrid_Core1()

#Processor 2 layout
lbl_Core2 = tk.Label(master=frame_Core2, text="CORE 2",font="bold")
lbl_Core2.grid(row=5, column=0)
lbl_Core2.config(bg="yellow")

lbl_Core2_Wmiss = tk.Label(master=frame_Core2,  relief=tk.RAISED,text="write miss",font="bold" )
lbl_Core2_Wmiss.grid(row=5, column=1)

lbl_Core2_Rmiss = tk.Label(master=frame_Core2,relief=tk.RAISED, text="read miss", font="bold")
lbl_Core2_Rmiss.grid(row=5, column=2)

lbl_Core2_Inst = tk.Label(master=frame_Core2,relief=tk.RAISED, text="Instrucción", font="bold")
lbl_Core2_Inst.grid(row=6, column=0)

lbl_Core2_InstData = tk.Label(master=frame_Core2,relief=tk.RAISED, text=handler.p2.instruction, font="bold")
lbl_Core2_InstData.grid(row=6, column=1)

generateGrid_Core2()


#Processor 3 layout
lbl_Core3 = tk.Label(master=frame_Core3, text="CORE 3",font="bold")
lbl_Core3.grid(row=5, column=0)
lbl_Core3.config(bg="yellow")

lbl_Core3_Wmiss = tk.Label(master=frame_Core3,  relief=tk.RAISED,text="write miss",font="bold" )
lbl_Core3_Wmiss.grid(row=5, column=1)

lbl_Core3_Rmiss = tk.Label(master=frame_Core3, relief=tk.RAISED, text="read miss", font="bold")
lbl_Core3_Rmiss.grid(row=5, column=2)

lbl_Core3_Inst = tk.Label(master=frame_Core3,relief=tk.RAISED, text="Instrucción", font="bold")
lbl_Core3_Inst.grid(row=6, column=0)

lbl_Core3_InstData = tk.Label(master=frame_Core3,relief=tk.RAISED, text=handler.p3.instruction, font="bold")
lbl_Core3_InstData.grid(row=6, column=1)

generateGrid_Core3()

#Processor 4 layout
lbl_Core4 = tk.Label(master=frame_Core4, text="CORE 4",font="bold")
lbl_Core4.grid(row=5, column=0)
lbl_Core4.config(bg="yellow")

lbl_Core4_Wmiss = tk.Label(master=frame_Core4,  relief=tk.RAISED,text="write miss",font="bold" )
lbl_Core4_Wmiss.grid(row=5, column=1)

lbl_Core4_Rmiss = tk.Label(master=frame_Core4, relief=tk.RAISED, text="read miss", font="bold")
lbl_Core4_Rmiss.grid(row=5, column=2)

lbl_Core4_Inst = tk.Label(master=frame_Core4,relief=tk.RAISED, text="Instrucción", font="bold")
lbl_Core4_Inst.grid(row=6, column=0)

lbl_Core4_InstData = tk.Label(master=frame_Core4,relief=tk.RAISED, text=handler.p4.instruction, font="bold")
lbl_Core4_InstData.grid(row=6, column=1)

generateGrid_Core4()

#Memory layout
generateGrid_Mem()
lbl_Mem = tk.Label(master=frame_Mem, text="Memory",font="bold")
lbl_Mem.grid()
lbl_Mem.config(bg="yellow")



frame_Core1.grid(row=1, column=0, padx=10, pady=15)
frame_Core2.grid(row=1, column=1, padx=10, pady=15)
frame_Core3.grid(row=2, column=0, padx=10, pady=10)
frame_Core4.grid(row=2, column=1, padx=10, pady=10)
frame_Mem.grid(row=1, column=3, rowspan=2, padx=20)

frame_Menu.grid(row=0, column=0, columnspan=2)


window.mainloop()

