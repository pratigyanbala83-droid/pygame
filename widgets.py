from tkinter import *
window = Tk()
window.title ("demo world")
window.geometry("400x500")


Label (window , text="hi!  how are you? ",bg = "green").pack()
Label (window , text="whats your name?",bg = "cyan").pack()


user = Entry(window)
user.pack()

box = Text(window, height=4 , width=40 , bg ="pink")
box.pack()

def dis():
    name = user.get()
    box.delete("1.0",END)
    box.insert(END,"hello there!"+name+"\n")
    box.insert(END,"This are some examples of widgets")


Button(window , text="click me",command=dis ).pack()

window.mainloop()
