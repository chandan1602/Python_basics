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
#img = PhotoImage(file = "Yantrix.gif")-----in b1 write image=img
b1=Button(mainW, text="Continue",bg="light grey",font="110%",width="6", height="1", activeforeground="dark blue",activebackground="#d3d3d3", command=helloCallBack)
b1.place(x=110, y=100)

#Canvas
w = Canvas(mainW, width=300, height=60)
w.place(x=0, y=130)
canvas_height = 20
canvas_width = 300
y = int(canvas_height/2)
w.create_line(0, y, canvas_width, y)

#Frame
frame_1 = Frame(mainW)
frame_1.place(x=0, y=160)
bottomframe = Frame(mainW)
bottomframe.place(x=0, y=190, side=BOTTOM)
redbutton = Button(frame, text = 'Red', fg='red')
redbutton.place(x=0, y=220, side=LEFT)

mainW.mainloop()

