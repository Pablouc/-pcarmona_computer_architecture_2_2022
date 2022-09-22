import tkinter as tk

window =tk.Tk()
window.configure(width=1000, height=1000)

greeting = tk.Label(text="Protocolo para coherencia de caché")
greeting.pack()

#Top frame with the menu
frame_Menu=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)

#Creating 4 frames, one for each core
frame_Core1=tk.Frame(master=window, width=100, height=100, relief=tk.RAISED, borderwidth=5)
frame_Core2=tk.Frame(master=window, width=100, height=100, relief=tk.RAISED, borderwidth=5)
frame_Core3=tk.Frame(master=window, width=100, height=100, relief=tk.RAISED, borderwidth=5)
frame_Core4=tk.Frame(master=window, width=100, height=100, relief=tk.RAISED, borderwidth=5)

#Creating the menu
btn_Continuous=tk.Button(master=frame_Menu,text="Continuo")
btn_Continuous.pack(side=tk.LEFT)

btn_Pause=tk.Button(master=frame_Menu, text="Pausa", bg="red")
btn_Pause.pack(side=tk.LEFT)

btn_Step_by_Step=tk.Button(master=frame_Menu, text="Paso a paso")
btn_Step_by_Step.pack(side=tk.LEFT)

lbl_Inst = tk.Label(master=frame_Menu, text="Instrucción")
lbl_Inst.pack(side=tk.LEFT)

input_Inst = tk.Entry(master=frame_Menu)
input_Inst.pack(side=tk.LEFT)
#To get input_Inst data
# entry.get()

btn_sendInst=tk.Button(master=frame_Menu,text="Enviar") 
btn_sendInst.pack(side=tk.LEFT)


lbl_Core1 = tk.Label(master=frame_Core1, text="CORE 1")
lbl_Core1.pack()

lbl_Core2 = tk.Label(master=frame_Core2, text="CORE 2")
lbl_Core2.pack()

lbl_Core3 = tk.Label(master=frame_Core3, text="CORE 3")
lbl_Core3.pack()

lbl_Core4 = tk.Label(master=frame_Core4, text="CORE 4")
lbl_Core4.pack()

frame_Menu.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
frame_Core1.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)
frame_Core2.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)    
frame_Core3.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)
frame_Core4.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)



window.mainloop()
