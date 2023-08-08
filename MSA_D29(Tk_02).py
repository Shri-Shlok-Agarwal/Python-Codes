#
# DAY 29

#----------+
# TKINTER  |
#----------+

from tkinter import *


#Use of Show
"""top = Tk()
top.geometry("300x200")

enty0= Entry(top,width="25")
enty0.place(x=50,y=40)

enty1= Entry(top,bg="lime")
enty1.place(x=50,y=70)

enty2= Entry(top,fg="white",show="*")
enty2.place(x=50,y=100)

top.mainloop()"""

#Use of Frame
"""top = Tk()
top.geometry("300x200")

tframe= Frame(top,width="100",height="100",bg="pink")
tframe.pack()

lframe= Frame(top,width="100",height="50",bg="red")
lframe.pack(side=LEFT)

rframe= Frame(top,width="100",height="50",bg="green")
rframe.pack(side=RIGHT)

#lbl= Label(lframe,text="LOdu",fg="brown")
#lbl.pack(side= RIGHT)

#lbl2= Label(rframe,text="Vishal dale",fg="blue")
#lbl2.pack(side = LEFT)

btn= Button(tframe,text= "button",bg="white",fg="black")
btn.place(x=10,y=10)

top.mainloop()"""

#Use of Lable
"""top = Tk()
top.geometry("300x200")

lbl1=Label(top,text="Name")
lbl1.place(x=10,y=10)

lbl2=Label(top,text="Password",bg="black",fg="white",borderwidth=6,relief=RAISED)
lbl2.place(x=10,y=40)

lbl3=Label(top,text="Age",padx=10,pady=10,bg="lime")
lbl3.place(x=10,y=70)

top.mainloop()"""

#Use of LISTBOX
"""top = Tk()
top.geometry("300x200")
top.title("LISTSSSS")
lbl1 = Label(top,text = "List of colours",fg = "white",bg ="black") 
lbl1.place(x=10,y=10)
lb = Listbox(top,height=5)
lb.insert(1,"Red")
lb.insert(2,"Yellow")
lb.insert(3,"black")
lb.insert(4,"purple")
lb.place(x=10,y=30)

lbl2 = Label(top,text="List of fruits",fg="blue",bg="yellow")
lbl2.place(x=160,y=10)
lb1=Listbox(top,height=5)
lb1.insert(1,"AAM")
lb1.insert(2,"IMLI")
lb1.insert(3,"KADUA")
lb1.insert(4,"LAUDA")
lb1.place(x=160,y=30)

top.mainloop()"""

# Use of RadioButton
"""top= Tk()
top.geometry("200x100")
radio = IntVar()

rbtn1 = Radiobutton(top,text="Red",variable=radio,value="1")
rbtn1.place(x=10,y=10)

rbtn2 = Radiobutton(top,text="Green",variable=radio,value="2")
rbtn2.place(x=10,y=30)

rbtn3 = Radiobutton(top,text="Blue",variable=radio,value="3")
rbtn3.place(x=10,y=50)

top.mainloop()"""

#Use of Text
"""top = Tk()
top.title("Address")
top.geometry("300x200")
a
lb1=Label(top,text="Address :",fg="red",bg="yellow")
lb1.place(x=10,y=10)

dtxt= Text(top,width=15,height=5)
txt.place(x=10,y=40)

top.mainloop()"""

#Use of TopLevel
"""top=Tk()
top.geometry("300x200")

def func():
    chld = Toplevel(top)
    chld.mainloop()

btn1 = Button(top,text ="Open",width=10,command=func)
btn1.place(x=40,y=50)

top.mainloop()"""
