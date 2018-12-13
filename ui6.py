from tkinter import *
 
window = Tk()
 
window.title("Astrid ")
 
window.geometry('350x200')
 
lbl = Label(window, text="Time")
 
lbl.grid(column=0, row=0)
btn = Button(window, text="00:01")
 
btn.grid(column=0, row=1)
 
chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Packet Received', var=chk_state)
 
chk.grid(column=0, row=2)
chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='url', var=chk_state)
 
chk.grid(column=0, row=3)

lbl = Label(window, text="Status:OK")
 
lbl.grid(column=0, row=4)
 
 
 
window.mainloop()
