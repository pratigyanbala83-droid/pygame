from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

win=Tk()

win.geometry("700x750")
win.title("notepad")

def openfile():
    path=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if path:
        txt.delete(1.0,END)
        with open(path)as f:
            txt.insert(END,f.read())


def savefile():
    path=asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if path:
        with open(path,"w")as f:
            f.write(txt.get(1.0,END))

txt=Text(win)
frame=Frame(win)


Button(frame,text="OPEN",command=openfile).pack()
Button(frame,text="SAVE",command=savefile).pack()

frame.pack(side="left",fill="y")
txt.pack(side="right",expand=True,fill="both")


win.mainloop()