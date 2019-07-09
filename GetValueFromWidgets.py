from tkinter import *


mainW=Tk()
mainW.title("First GUI")
mainW.geometry("500x500")
mainW.resizable(0,0)


##################################################
def getValues():
    #get Data from Entry
    name=e1.get()
    a=int(e2.get())
    c=a+a

    #RadioButton
    gender=gen.get()

    
    #Checkbutton
    qual=""
    if(q1.get()==1):
        qual=qual+' +2 '
    if(q2.get()==1):
        qual=qual+' grad '
    #display text on Label: configure()
    l5.configure(text=name+"\n"+str(c)+"\nGender is "+gender+"\nQual:"+qual)


####################################################

l1=Label(mainW,text="Enter Name")
l1.grid(row=0,column=0)

e1=Entry(mainW)
e1.grid(row=0,column=1)

l2=Label(mainW,text="Enter A")
l2.grid(row=1,column=0)


e2=Entry(mainW)
e2.grid(row=1,column=1)


l3=Label(mainW,text="Select Gender")
l3.grid(row=2,column=0)

#Radiobutton
gen=StringVar()
r1=Radiobutton(mainW,text="Male",variable=gen,value="M")
r1.grid(row=2,column=1)

r2=Radiobutton(mainW,text="FeMale",variable=gen,value="F")
r2.grid(row=2,column=2)


l4=Label(mainW,text="Qualification")
l4.grid(row=3,column=0)

#Checkbutton
q1=IntVar()
q2=IntVar()

c1=Checkbutton(mainW,text="+2",variable=q1,onvalue=1,offvalue=0)
c1.grid(row=3,column=1)

c2=Checkbutton(mainW,text="grad",variable=q2,onvalue=1,offvalue=0)
c2.grid(row=3,column=2)

#Button
b1=Button(mainW,text="Submit",command=getValues)
b1.grid(row=4,column=0)

l5=Label(mainW)
l5.grid(row=5,column=0)

mainW.mainloop()
