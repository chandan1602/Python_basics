from tkinter import *
import sqlite3
con=sqlite3.connect("form_db")
if con:
    print("Database Connected")
else:
    print("Error connecting Database!!")

#con.execute("create table form (name text,age int,gender text,qual text)")
cur=con.cursor()
##################################################################3

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
    #l5.configure(text=name+"\n"+str(c)+"\nGender is "+gender+"\nQual:"+qual)

    #Inserting values into the databse
    con.execute("insert into form(name,age) values('%s',%d)"%(e1.get(), int(e2.get())))
    con.commit()
    print("Data Inserted!!")

    #Displaying values from database
    cur.execute("select * from form")
    print("NAME            AGE")
    print("-------------------")
    for values in cur:
        print(values[0], "      ",values[1])
 
def deleteRecord():
    nameDel=e5.get()
    #Database commands
    con.execute("delete from form where name='%s'"%(nameDel))
    con.commit()
    print("Data deleted!!")

    #Displaying values from database
    cur.execute("select * from form")
    print("NAME            AGE")
    print("-------------------")
    for values in cur:
        print(values[0], "      ",values[1])    
    

####################################################

l1=Label(mainW,text="Enter Name")
l1.grid(row=0,column=0)

e1=Entry(mainW)
e1.grid(row=0,column=1)

l2=Label(mainW,text="Enter Age")
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

'''
l5=Label(mainW)
l5.grid(row=5,column=0)
'''

#Delete label
l5=Label(mainW,text="Enter Name")
l5.grid(row=5,column=0)

e5=Entry(mainW)
e5.grid(row=5,column=1)

#Button
b2=Button(mainW, text="Delete Record", command=deleteRecord)
b2.grid(row=6,column=0)


mainW.mainloop()
