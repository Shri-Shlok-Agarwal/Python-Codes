#___________________________________________________________________________________________________
# DAY 28

#---------+
# TKINTER |
#---------+
from tkinter import *

# First Trial Tkinter Program
"""import tkinter
top = tkinter.Tk()  #creating the application main window.
top.title("Welcome")    #title of the main window.
top.geometry("599x500") #size of main window.
top.mainloop()"""

#_______________________________________________
# PACK, PLACE and GRID METHOD

# Use of pack method to place button 
"""from tkinter import *
top=Tk()
top.title("Place Method")
top.geometry("300x200")
bt1= Button(top,text = "Login left")
bt1.pack(side = LEFT)
bt2= Button(top,text = "Login up")
bt2.pack(side = TOP)
bt3= Button(top,text = "Login right")
bt3.pack(side = RIGHT)
bt4= Button(top,text = "Login down")
bt4.pack(side = BOTTOM)
top.mainloop()"""

# Use of Grid Method to Place Button,Labels etc
"""parent=Tk()
parent.title("Students Details")
parent.geometry("400x300")

name=Label(parent, text = "Name : ")
name.grid(row=0,column=0,pady=10,padx=5)

e1= Entry(parent)
e1.grid(row=0,column=1)

regno = Label(parent, text = "RegNo. : ")
regno.grid(row=1,column=0,pady=10,padx=5)

e1= Entry(parent)
e1.grid(row=1,column=1)

btn = Button(parent,text = "Submit")
btn.grid(row=3,column=1)

parent.mainloop()"""

# Use of Place Method to Place Button,Labels etc
"""parent=Tk()
parent.title("Students Details")
parent.geometry("400x300")

name=Label(parent, text = "Name : ")
name.place(x=50,y=50)

e1= Entry(parent)
e1.place(x=100,y=50)

regno = Label(parent, text = "RegNo. : ")
regno.place(x=50,y=100)

e1= Entry(parent)
e1.place(x=100,y=100)

btn = Button(parent,text = "Submit")
btn.place(x=100,y=150)

parent.mainloop()"""


#__________________________________________-
# USE OF BUTTON AND WORK in it

"""from tkinter import messagebox

top=Tk()
top.geometry("400x300")

def fun():
    messagebox.showinfo("Hello", "Blue Button Clicked")

btn1 = Button(top,text = "Red", bg="red", fg="white",width=10)
btn1.pack(side=LEFT)

btn2=Button (top, text="Green",bg="green",fg="white",width=10,height=5, activebackground= "lime")
btn2.pack(side=TOP)

btn3 = Button (top, text="yellow",bg="yellow",fg="black",padx=30,pady=30,command=fun)
btn3.pack(side = BOTTOM)

top.mainloop()"""

#__________________________________________________-
# USE OF CHECK_BUTTON AND WORK in it
"""top=Tk()
top.geometry("300x200")

cbtn1= Checkbutton(top, text="Red",fg="red")
cbtn1.pack()

cbtn2= Checkbutton (top, text="Green",fg="green", activebackground="orange")
cbtn2.pack()

cbtn3= Checkbutton(top, text="Blue",fg="blue",bg="yellow",width=10,height=3)
cbtn3.pack()

top.mainloop()"""

