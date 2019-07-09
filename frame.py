from tkinter import *

mainW=Tk()
mainW.title("First GUI")
mainW.geometry("500x500")
mainW.resizable(0,0)

#Frame
frame = Frame(mainW)
frame.pack()
bottomframe = Frame(mainW)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text = 'Red', fg='red')
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text = 'Green', fg='green')
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text = 'Blue', fg='blue')
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text = 'Black', fg='black')
blackbutton.pack(side=BOTTOM)

mainW.mainloop()
