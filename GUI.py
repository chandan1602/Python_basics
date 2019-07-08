from tkinter import *
import tkinter.messagebox as box

mainW=Tk()
mainW.title("First GUI")
mainW.geometry("500x500")
mainW.resizable(0,0)

'''
#Label
l0=Label(mainW, text="Welcome", bg='#B3B3B3', width='20')
l0.grid(row=0, column=1, columnspan=2)

#Label
l1=Label(mainW, text="Enter Name : ")
l1.grid(row=1, column=0)

#Entry
e1=Entry(mainW)
e1.grid(row=1, column=1)

#Label
l2=Label(mainW, text="Enter Age : ")
l2.grid(row=2, column=0)

#Entry
e2=Entry(mainW)
e2.grid(row=2, column=1)

#Button
b1=Button(mainW, text="Continue", command=exit)
b1.grid(row=3, column=0, columnspan=3)
'''

name = StringVar()
age = StringVar()

def helloCallBack():
    Name = name
    Age = age
    message = "Hello " + Name.get() + ". Your Age is set to be " + Age.get()
    box.showinfo( "Message 202(Accepted)", message)
    exit

#Label
l0=Label(mainW, text="Welcome", bg='#B3B3B3', width='62')
l0.place(x=0, y=0)

#Label
l1=Label(mainW, text="Enter Name : ")
l1.place(x=0, y=40)

#Entry
e1=Entry(mainW, textvariable = name)
e1.place(x=80, y=40)

#Label
l2=Label(mainW, text="Enter Age : ")
l2.place(x=0, y=70)

#Entry
e2=Entry(mainW, textvariable = age)
e2.place(x=80, y=70)

#Button
b1=Button(mainW, text="Continue", command=helloCallBack)
b1.place(x=110, y=100)

mainW.mainloop()

