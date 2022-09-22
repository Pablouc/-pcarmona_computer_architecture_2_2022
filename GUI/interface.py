import tkinter as tk


#Functions

def continuous_Flag(event):
    print("Continuous flag activated")

def pause_Flag(event):
    print("Pause flag activated")

def step_By_Step_Flag(event):
    print("Step by step flag activated")

def send_Flag(event):
    print("send instruction flag activated")

def generateGrid_Core1():
    for i in range(5):
        for j in range(4):
            gridFrame1 = tk.Frame(master=frame_Core1,relief=tk.RAISED,borderwidth=1)
            gridFrame1.grid(row=i, column=j, padx=5, pady=5)
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="State"
                        case 2: name="Address"
                        case 3: name="Data"
                    label = tk.Label(master=gridFrame1, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame1, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
             
            label = tk.Label(master=gridFrame1, text=f"0", width=8, height=2)
            label.pack()

def generateGrid_Core2():
    for i in range(5):
        for j in range(4):
            gridFrame2 = tk.Frame(master=frame_Core2,relief=tk.RAISED,borderwidth=1)
            gridFrame2.grid(row=i, column=j, padx=5, pady=5)
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="State"
                        case 2: name="Address"
                        case 3: name="Data"
                    label = tk.Label(master=gridFrame2, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame2, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
             
            label = tk.Label(master=gridFrame2, text=f"0", width=8, height=2)
            label.pack()


def generateGrid_Core3():
    for i in range(5):
        for j in range(4):
            gridFrame3 = tk.Frame(master=frame_Core3,relief=tk.RAISED,borderwidth=1)
            gridFrame3.grid(row=i, column=j, padx=5, pady=5)
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="State"
                        case 2: name="Address"
                        case 3: name="Data"
                    label = tk.Label(master=gridFrame3, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame3, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
             
            label = tk.Label(master=gridFrame3, text=f"0", width=8, height=2)
            label.pack()

def generateGrid_Core4():
    for i in range(5):
        for j in range(4):
            gridFrame4 = tk.Frame(master=frame_Core4,relief=tk.RAISED,borderwidth=1)
            gridFrame4.grid(row=i, column=j, padx=5, pady=5)
            if(i==0):
                if(j>0):
                    match j:
                        case 1: name="State"
                        case 2: name="Address"
                        case 3: name="Data"
                    label = tk.Label(master=gridFrame4, text=name, width=10, height=2)
                    label.pack()
                    continue
            if(i>0 ):
                if(j==0):
                    label = tk.Label(master=gridFrame4, text=f"Bloque {i}", width=10, height=2)
                    label.pack()
                    continue
             
            label = tk.Label(master=gridFrame4, text=f"0", width=8, height=2)
            label.pack()
        

window =tk.Tk()
window.geometry("1600x400")


#Top frame with the menu
frame_Menu=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

#Creating 4 frames, one for each core
frame_Core1=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
generateGrid_Core1()


frame_Core2=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
gridFrame_Core2 = tk.Frame(master=frame_Core2,relief=tk.RAISED,borderwidth=1)
generateGrid_Core2()

frame_Core3=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
gridFrame_Core3 = tk.Frame(master=frame_Core3,relief=tk.RAISED,borderwidth=1)
generateGrid_Core3()

frame_Core4=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
gridFrame_Core4 = tk.Frame(master=frame_Core4,relief=tk.RAISED,borderwidth=1)
generateGrid_Core4()

#Creating the menu
btn_Continuous=tk.Button(master=frame_Menu,text="Continuo")
btn_Continuous.pack(side=tk.LEFT,expand=True)
btn_Continuous.bind('<Button-1>', continuous_Flag)

btn_Pause=tk.Button(master=frame_Menu, text="Pausa", bg="red")
btn_Pause.pack( side=tk.LEFT,expand=True)
btn_Pause.bind('<Button-1>', pause_Flag)

btn_Step_by_Step=tk.Button(master=frame_Menu, text="Paso a paso")
btn_Step_by_Step.pack(side=tk.LEFT,expand=True)
btn_Step_by_Step.bind('<Button-1>', step_By_Step_Flag)

lbl_Inst = tk.Label(master=frame_Menu, text="Instrucción")
lbl_Inst.pack( side=tk.LEFT,expand=True)

input_Inst = tk.Entry(master=frame_Menu)
input_Inst.pack( side=tk.LEFT,expand=True)
#To get input_Inst data
# entry.get()

btn_sendInst=tk.Button(master=frame_Menu,text="Enviar") 
btn_sendInst.pack(side=tk.LEFT,expand=True)
btn_sendInst.bind('<Button-1>', send_Flag)

#Processor 1 layout

lbl_Core1 = tk.Label(master=frame_Core1, text="CORE 1", font="bold")
lbl_Core1.grid()
lbl_Core1.config(bg="yellow")

lbl_Core1_Wmiss = tk.Label(master=frame_Core1, text="write miss")
lbl_Core1_Wmiss.grid()

lbl_Core1_Rmiss = tk.Label(master=frame_Core1, text="read miss")
lbl_Core1_Rmiss.grid()

#Processor 2 layout
lbl_Core2 = tk.Label(master=frame_Core2, text="CORE 2",font="bold")
lbl_Core2.grid()
lbl_Core2.config(bg="yellow")

lbl_Core2_Wmiss = tk.Label(master=frame_Core2, text="write miss")
lbl_Core2_Wmiss.grid()

lbl_Core2_Rmiss = tk.Label(master=frame_Core2, text="read miss")
lbl_Core2_Rmiss.grid()


#Processor 3 layout
lbl_Core3 = tk.Label(master=frame_Core3, text="CORE 3",font="bold")
lbl_Core3.grid()
lbl_Core3.config(bg="yellow")

lbl_Core3_Wmiss = tk.Label(master=frame_Core3, text="write miss")
lbl_Core3_Wmiss.grid()

lbl_Core3_Rmiss = tk.Label(master=frame_Core3, text="read miss")
lbl_Core3_Rmiss.grid()


#Processor 4 layout
lbl_Core4 = tk.Label(master=frame_Core4, text="CORE 4",font="bold")
lbl_Core4.grid()
lbl_Core4.config(bg="yellow")

lbl_Core4_Wmiss = tk.Label(master=frame_Core4, text="write miss")
lbl_Core4_Wmiss.grid()

lbl_Core4_Rmiss = tk.Label(master=frame_Core4, text="read miss")
lbl_Core4_Rmiss.grid()

frame_Menu.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
frame_Core1.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)
frame_Core2.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)    
frame_Core3.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)
frame_Core4.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)



window.mainloop()
