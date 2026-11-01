from tkinter import *
from tkinter  import messagebox


win=Tk()


win.title("virus detector")
win.geometry("400x500")
win.configure(bg="thistle")

def msg():
    messagebox.showerror("Alert","Virus detected")


button=Button(bg="black",fg="beige",text="Search for any virus",command=msg)
button.place(x=15,y=50)



win.mainloop()