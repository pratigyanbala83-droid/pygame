from tkinter import *
window = Tk()
window.title("event handler")
window.geometry("549x649")

def button(event):
    print("button is clicked")
def charat(c):
    print(c.char)

button1= Button(bg="thistle",fg="aqua",text="click me!")
button1.pack()
window.bind("<Key>",charat)
button1.bind("<Button-1>",button)




window.mainloop()