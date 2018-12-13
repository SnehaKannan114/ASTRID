from tkinter import *

from tkinter import messagebox
window=Tk()
window.title("Astrid ")
 
window.geometry('350x200')
top = Tk()
top.geometry("100x100")
lbl = Label(window, text="Time")
 
lbl.grid(column=0, row=0)
btn = Button(window, text="00:01")
 
btn.grid(column=0, row=1)
def alert():
   messagebox.showinfo("Alert!", "There is some attack detected")

B1 = Button(top, text = "Alert!", command = alert)
B1.place(x = 35,y = 50)

top.mainloop()
