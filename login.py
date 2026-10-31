from tkinter import *
window=Tk()
window.title("Login app")
window.geometry("500x500")

frame = Frame(window,height=200,width=300,bg="cyan")

label1=Label(frame,text="Full name:",bg="lavender",fg="black",width=12)
label2=Label(frame,text="Email adress:",bg="lavender",fg="black",width=12)
label3=Label(frame,text="Password:",bg="lavender",fg="black",width=12)

entry1=Entry(frame)
entry2=Entry(frame)
entry3=Entry(frame,show="*")

def display():
    name=entry1.get()
    greet=" hey "+name
    msg="\nCongratulations on your new account"
    text.insert(END,greet)
    text.insert(END,msg)
    
text=Text(bg="beige",width=45)
button=Button(frame,text="Click me!",command=display,bg="blue")

frame.place(x=20,y=0)
label1.place(x=20,y=20)
entry1.place(x=150,y=20)
label2.place(x=20,y=80)
entry2.place(x=150,y=80)
label3.place(x=20,y=140)
entry3.place(x=150,y=140)
button.place(x=120,y=180)
text.place(y=250)

window.mainloop()






    