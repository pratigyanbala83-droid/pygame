from tkinter import *
window = Tk()
window.title("Number pad")
window.geometry("300x400")
nums=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]

for i in range(0,4):
    window.columnconfigure(i,weight=1,minsize = 75)
    window.rowconfigure(i,weight=1,minsize = 50)
    for  j in range(0,3):
        frame = Frame(window,relief = RAISED, borderwidth = 2)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg="lavender")
        label.pack()
        


window.mainloop()
