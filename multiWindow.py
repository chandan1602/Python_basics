from tkinter import *

class A:
    def __init__(self,parent):
        self.root=parent
        self.win1 = Button(self.root, text="window 1",command=self.window1)
        self.win1.pack()

        self.win2 = Button(self.root, text="window 2",command=self.window2)
        self.win2.pack()

    def window1(self):
        t1=Toplevel(mainW)
        w1=Window1(t1)

    
    def window2(self):
        t1=Toplevel(mainW)
        w1=Window2(t1)

class Window1:
    def __init__(self,parent):
        self.root=parent
        self.l1 = Button(self.root, text="welcome 1")
        self.l1.pack()

class Window2:
    def __init__(self,parent):
        self.root=parent
        self.root.title("Window2")
        self.root.geometry("500x500")
        self.l1 = Button(self.root, text="welcome 2")
        self.l1.pack()



mainW=Tk()
mainW.title("First GUI")
mainW.geometry("500x500")

obj=A(mainW)

mainW.resizable(0,0)
