from tkinter import *
from tkinter import messagebox

win= Tk()
win.title("MONEY CALCULATOR")
win.geometry("540x520")
win.configure(bg="light green")

Label(win,text="Money calculator",bg="light green").pack(pady=15)
Label(win,text="Enter total amount",bg="light green").pack()
entry = Entry(win)
entry.pack(pady=10)

def calculator():
    try:
        amount=int(entry.get())
        if amount<0:
            messagebox.showerror("Error","Enter a possitive amount")
            return
        n2000 = amount // 2000
        amount %= 2000
        n500 = amount // 500
        amount %= 500
        n100 = amount // 100

        result.config(text=f"2000 Notes:{n2000}\n"
                      f"500 Notes:{n500}\n"
                      f"100 Notes:{n100}\n")

    except ValueError:
        messagebox.showerror("Error","Enter a valid number")


Button(win,text="Calculator",command=calculator).pack(pady=15)
result = Label(win,text = "", bg = "light green",justify=LEFT)
result.pack(pady=10)
win.mainloop()

   
                                                   
        
        
            
