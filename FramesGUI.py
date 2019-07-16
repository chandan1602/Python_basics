from tkinter import *
import sqlite3
import tkinter.messagebox as box
#########################################################################
con=sqlite3.connect("project1db")
if con:
    print("Database Connected")
else:
    print("Error connecting Database!!")

#con.execute("create table signup (name text,age int,gender text,qual text, pass text, ConPass text)")
#con.execute("create table contacts (name text, code text, number int)")
cur=con.cursor()
#########################################################################

class A:#step2
    def __init__(self,parent):
        self.login=parent

        self.l0=Label(self.login, text="LOGIN", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.l=Label(self.login)
        self.l.grid(row=1, column=0)
        
        self.l1=Label(self.login,text="Username or Email-Id : ", width=20)
        self.l1.grid(row=2,column=0)
        self.e1=Entry(self.login)
        self.e1.grid(row=2,column=1, columnspan=2)

        self.passL=Label(self.login, text="Enter Password", width=20)
        self.passL.grid(row=3, column=0)
        self.passI=Entry(self.login, show="**")
        self.passI.grid(row=3,column=1, columnspan=2)

        self.linebreak = Label(self.login)
        self.linebreak.grid(row=4, column=0)

        self.loginB = Button(self.login, text="Login",bg="#353535",foreground="#fff", command=self.window1)
        self.loginB.grid(row=5, column=0)

        self.win2 = Button(self.login, text="Signup",bg="#353535", foreground="#fff", command=self.window2)
        self.win2.grid(row=5, column=1)
        

    def window1(self):
        username=self.e1.get()
        password=self.passI.get()
        if username=='' or password=='':
            box.showinfo("Alert", "All the fields are required")#if fields are empty
        cur.execute("select * from signup where name=?", (username,))
        for values in cur:
            
            if values[4]!=password:
                box.showinfo("WARNING!!", "Password Mismatch")#wrong password
            else:
                message="Welcome " + username + "!!"
                box.showinfo("Welcome Back ", message)
                t1=Toplevel(mainW)
                w1=Window1(t1)
                
        cur.execute("select exists(select * from signup where name=?)", (username, ))#if username does not exist
        for values in cur:
            if values[0]==0 and (username!='' and password!=''):#excluding conditions when fields are empty
                box.showinfo("SORRY", "You are not signed up yet!")
        
    def window2(self):
        t1=Toplevel(mainW)
        w1=Window2(t1)

#########################################################################################################

class Window1:
    def __init__(self,parent):
        self.root=parent
        self.root.title("Window 1")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        #self.root.frame=Frame(self.root,width=200,height=200,bg='grey')
        #self.root.frame.pack()

        self.l0=Label(self.root, text="WELCOME", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.linebreak = Label(self.root)
        self.linebreak.grid(row=1, column=0)
        
        self.l1 = Button(self.root, text="READ",bg="#353535",foreground="#fff",command=self.readData)
        self.l1.grid(row=2, column=0)
        
        self.l2 = Button(self.root, text="DELETE",bg="#353535",foreground="#fff",command=self.delData)
        self.l2.grid(row=2, column=1)

        self.linebreak = Label(self.root)
        self.linebreak.grid(row=3, column=0)
    
        self.l2 = Button(self.root, text="INSERT",bg="#353535",foreground="#fff",command=self.insertData)
        self.l2.grid(row=4, column=0)
    
        self.l2 = Button(self.root, text="UPDATE",bg="#353535",foreground="#fff",command=self.updateData)
        self.l2.grid(row=4, column=1)
     
        
#################
    def readData(self):
        t1=Toplevel(mainW)
        r1=readData(t1)

    def insertData(self):
        t1=Toplevel(mainW)
        i1=insertData(t1)
    
    def delData(self):
        t1=Toplevel(mainW)
        d1=delData(t1)
        '''
        self.root.frame=Frame(self.root,width=200,height=200,bg='grey')
        self.root.frame.pack()
        self.l1=Label(self.root.frame,text="enter id")
        self.l1.pack()
        self.l2=Label(self.root.frame,text="enter name")
        self.l2.pack()
        '''

    def updateData(self):
        t1=Toplevel(mainW)
        u1=updateData(t1)        
###################
       

################################################################################################
class insertData:
    def __init__(self, parent):
        self.insert=parent
        self.insert.title("Data Insertion")
        self.insert.geometry("500x500")
        self.insert.resizable(0,0)

        self.l0=Label(self.insert, text="INSERT YOUR DATA", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.linebreak = Label(self.insert)
        self.linebreak.grid(row=1, column=0)

        self.l1=Label(self.insert,text="Enter Name")
        self.l1.grid(row=2,column=0)
        self.e1=Entry(self.insert)
        self.e1.grid(row=2,column=1, columnspan=2)

        self.l2=Label(self.insert,text="Enter Country Code")
        self.l2.grid(row=3,column=0)
        self.e2=Entry(self.insert)
        self.e2.grid(row=3,column=1, columnspan=2)

        self.l3=Label(self.insert,text="Enter Contact Number")
        self.l3.grid(row=4,column=0)
        self.e3=Entry(self.insert)
        self.e3.grid(row=4,column=1, columnspan=2)

        self.b1 = Button(self.insert, text="INSERT",bg="#353535",foreground="#fff",command=self.saveData)
        self.b1.grid(row=5, column=0)

###################
    def saveData(self):
        #fetching values
        name = self.e1.get()
        code = self.e2.get()
        number = self.e3.get()

        if name=='' or code=='' or number=='':
            box.showinfo("ALERT", "All the fields are mandatory!!")#all fields condition
        if len(number)!=10 and number!='':
            box.showinfo("ALERT", "Contact Number doesn't have 10 numbers!!")#wrong contact number

        if name!='' and code!='' and number!='' and len(number)==10:
            con.execute("insert into contacts values('%s','%s',%d)"%(name, code, int(number)))
            con.commit()
            print("Data Inserted!!")                

            #Displaying values from database
            cur.execute("select * from contacts")
            print("NAME             COUNTRY-CODE           CONTACT-NUMBER")
            print("-----------------------------------------------------------------")
            for values in cur:
                print(values[0], "            ",values[1], "        ", values[2])

            box.showinfo("ALL SET", "Data insertion Successful!!")#successful insertion
            self.insert.destroy()

###################

################################################################################################

class delData:
    def __init__(self, parent):
        self.delete=parent
        self.delete.title("Here is your data!")
        self.delete.geometry("500x500")
        self.delete.resizable(0,0)

        self.l0=Label(self.delete, text="DELETE YOUR DATA", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.linebreak = Label(self.delete)
        self.linebreak.grid(row=1, column=0)

        self.l1=Label(self.delete,text="Enter Name")
        self.l1.grid(row=2,column=0)
        self.e1=Entry(self.delete)
        self.e1.grid(row=2,column=1, columnspan=2)

        self.linebreak = Label(self.delete)
        self.linebreak.grid(row=3, column=0)

        self.b1 = Button(self.delete, text="DELETE",bg="#353535",foreground="#fff",command=self.deleteData)
        self.b1.grid(row=4, column=0, columnspan=2)      
###################
        
    def deleteData(self):
        #fetching values
        name=self.e1.get()

        #database
        if name=='':
            box.showinfo("ALERT", "All the fields are required!!")
        cur.execute("select exists(select * from contacts where name=?)",(name,))
        for values in cur:
            if values[0]==0 and name!='':
                box.showinfo("ALERT", "MATCHING NAME NOT FOUND IN THE DATABASE!!")
            if values[0]==1:
                con.execute("delete from contacts where name='%s'"%(name))
                con.commit()
                box.showinfo("ALL DONE!", "The Contact has been deleted successfully!!")
                self.delete.destroy()
                #Displaying values from database
                cur.execute("select * from contacts")
                print("NAME             COUNTRY-CODE           CONTACT-NUMBER")
                print("-----------------------------------------------------------------")
                for values in cur:
                    print(values[0], "            ",values[1], "        ", values[2])


###################

################################################################################################
class updateData:
    def __init__(self, parent):
        self.update=parent
        self.update.title("Here is your data!")
        self.update.geometry("500x500")
        self.update.resizable(0,0)

        self.l0=Label(self.update, text="UPDATE YOUR DATA", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.linebreak = Label(self.update)
        self.linebreak.grid(row=1, column=0)

        self.l1=Label(self.update,text="Enter Name")
        self.l1.grid(row=2,column=0)
        self.e1=Entry(self.update)
        self.e1.grid(row=2,column=1, columnspan=2)

        self.l2=Label(self.update,text="Enter Country Code")
        self.l2.grid(row=3,column=0)
        self.e2=Entry(self.update)
        self.e2.grid(row=3,column=1, columnspan=2)

        self.l3=Label(self.update,text="Enter Contact Number")
        self.l3.grid(row=4,column=0)
        self.e3=Entry(self.update)
        self.e3.grid(row=4,column=1, columnspan=2)

        self.b1 = Button(self.update, text="UPDATE",bg="#353535",foreground="#fff",command=self.saveData)
        self.b1.grid(row=5, column=0)

    
################################################################################################
    def saveData(self):
        #fetching values
        name = self.e1.get()
        code = self.e2.get()
        number = self.e3.get()

        #database
        if name=='' or code=='' or number=='':
            box.showinfo("ALERT", "All the fields are Mandatory!!")
        cur.execute("select exists(select * from contacts where name=?)", (name,))
        for values in cur:
            if values[0]==0 and name!='' and code!='' and number!='':
                box.showinfo("ALERT", "The entered name does not exist in the database")
            if values[0]==1 and name!='' and code!='' and number!='':
                con.execute("update contacts set code=? where name=?", (code, name, ))
                con.commit()
                con.execute("update contacts set number=? where name=?", (number, name, ))               
                con.commit()
                box.showinfo("All Done", "Contact Updated Successfully!!")
                self.update.destroy()
                #Displaying values from database
                cur.execute("select * from contacts")
                print("NAME             COUNTRY-CODE           CONTACT-NUMBER")
                print("-----------------------------------------------------------------")
                for values in cur:
                    print(values[0], "            ",values[1], "        ", values[2])

                
###################
   
###################
    
################################################################################################
class readData:
    def __init__(self, parent):
        self.read=parent
        self.read.title("Here is your data!")
        self.read.geometry("500x500")
        self.read.resizable(0,0)

        self.l0=Label(self.read, text="WELCOME TO YOUR DATA", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.linebreak = Label(self.read)
        self.linebreak.grid(row=1, column=0)
        
        self.data=Label(self.read)
        self.data.grid(row=2, column=0)

        #Displaying values from database
        cur.execute("select * from signup")
        #self.data.configure(text="NAME                        AGE           GENDER         QUALIFICATION       PASSWORD")
        #self.data.configure(text="-------------------------------------------------------------------------------------")
        for values in cur:
            net=values[0]+ "      "+str(values[1])+ "      "+ values[2]+ "      "+ values[3]+ "      "+ values[4]
            self.data.configure(text=net)


        
 

#################################################################################################
class Window2:
    def __init__(self,parent):
        self.root=parent
        self.root.title("Window2")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        
        self.l0=Label(self.root, text="SIGNUP", bg='#B3B3B3', width='62')
        self.l0.grid(row=0, column=0, columnspan=3)

        self.l=Label(self.root)
        self.l.grid(row=1, column=0)
        
        self.l1=Label(self.root,text="Enter Username or Email-Id : ")
        self.l1.grid(row=2,column=0)
        self.e1=Entry(self.root)
        self.e1.grid(row=2,column=1, columnspan=2)

        self.l2=Label(self.root,text="Enter Age")
        self.l2.grid(row=3,column=0)
        self.e2=Entry(self.root)
        self.e2.grid(row=3,column=1, columnspan=2)

        self.passL=Label(self.root, text="Create Password")
        self.passL.grid(row=4, column=0)
        self.passI=Entry(self.root, show="**")
        self.passI.grid(row=4,column=1, columnspan=2)

        self.confirmPassL=Label(self.root, text="Confirm Password")
        self.confirmPassL.grid(row=5, column=0)
        self.confirmPassI=Entry(self.root, show="**")
        self.confirmPassI.grid(row=5,column=1, columnspan=2)
            
        
        self.l3=Label(self.root,text="Select Gender")
        self.l3.grid(row=6,column=0)
         
        #Radiobutton
        self.gen=StringVar()
        self.r1=Radiobutton(self.root,text="Male",variable=self.gen,value="M")
        self.r1.grid(row=6,column=1, columnspan=1)

        self.r2=Radiobutton(self.root,text="Female",variable=self.gen,value="F")
        self.r2.grid(row=6,column=2)


        self.l4=Label(self.root,text="Qualification")
        self.l4.grid(row=7,column=0)

        #Checkbutton
        self.q1=IntVar()
        self.q2=IntVar()

        self.c1=Checkbutton(self.root,text="+2",variable=self.q1,onvalue=1,offvalue=0)
        self.c1.grid(row=7,column=1)

        self.c2=Checkbutton(self.root,text="grad",variable=self.q2,onvalue=1,offvalue=0)
        self.c2.grid(row=7,column=2)

        self.linebreak = Label(self.root)
        self.linebreak.grid(row=8, column=0)
        
        #Button
        self.b1=Button(self.root,text="Signup",bg="#353535",foreground="#fff",command=self.getValues)
        self.b1.grid(row=9,column=0, columnspan=3)

      
###################
    def getValues(self):     
        #get Data from Entry
        name=self.e1.get()
        age=self.e2.get()
        
        #RadioButton
        gender=self.gen.get()

        
        #Checkbutton
        qual=""
        if(self.q1.get()==1):
            qual=qual+' +2 '
        if(self.q2.get()==1):
            qual=qual+' grad '

        #Password
        password = self.passI.get()
        confirmedPass = self.confirmPassI.get()
        if password!=confirmedPass and password!='' and confirmedPass!='':#password not matching
            box.showinfo("Alert", "Password and Confirm-Password does not match")

        #CALLBACKS
        if password==confirmedPass and name!='' and age!='' and gender!='' and password!='' and confirmedPass!='':
            #inserting data into the database
            con.execute("insert into signup values('%s',%d,'%s','%s','%s','%s')"%(name, int(age), gender, qual, password, confirmedPass))
            con.commit()
            print("Data Inserted!!")

            #Displaying values from database
            cur.execute("select * from signup")
            print("NAME                        AGE           GENDER         QUALIFICATION       PASSWORD")
            print("-------------------------------------------------------------------------------------")
            for values in cur:
                print(values[0], "      ",values[1], "      ", values[2], "      ", values[3], "      ", values[4])


            title="Congratulations " + name
            box.showinfo(title, "You have Successfully Signed Up")#successful signup
            self.root.destroy()

        if name=='' or age=='' or gender=='' or password=='' or confirmedPass=='':
            box.showinfo("Alert", "All sections are Required")#any field is empty

        
###################
        


mainW=Tk()
mainW.title("First GUI")
mainW.geometry("500x500")

obj=A(mainW)#step1

mainW.resizable(0,0)
