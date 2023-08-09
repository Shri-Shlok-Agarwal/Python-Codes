#establishing connection
import  mysql.connector

#importing module
from tkinter import *

#importing connection and creating database if not created
mydb = mysql.connector.connect( host='localhost',user='root', password='')
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
db=list(mycursor)
if (('fitnesslogbuddy',) not in db):
    mycursor.execute("CREATE DATABASE FitnessLogBuddy")
else:
    pass

def open2win():

    user=UID.get()
        #importing connection and creating UserId if not created
    mydb = mysql.connector.connect( host='localhost',user='root', password='',database="fitnesslogbuddy")
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    tbl=list(mycursor)

    global nuser
    nuser=user
    if ((nuser.lower(),)not in tbl):   #(NewUser,)
        x=("CREATE TABLE "+nuser+"(SrN INT AUTO_INCREMENT PRIMARY KEY,Date VARCHAR(100),Workout VARCHAR(300),Duration VARCHAR(100),Calories_Burned VARCHAR(100),Height DOUBLE(50,2),Weight DOUBLE(50,2))")
        mycursor.execute(x)
        mydb.commit()
    else:
        pass

    #defining Input function
    def Input():
        #getting form data
        date1=date.get()
        workout1=workout.get()
        duration1=duration.get()
        calorie1=calorie.get()
        height1=height.get()
        weight1=weight.get()
        
        #applying empty validation
        if date1=='' or workout1==''or duration1=='' or calorie1=='' or height1==None or weight1==None :
            message.set("Fill the Empty Field!!!")
        else:
            # Creating a cursor object using the cursor() method
            mycursor = mydb.cursor()
            # Preparing SQL query to INSERT a record into the Table.
            insert_stmt = ("INSERT INTO "+nuser+"(Date, Workout, Duration, Calories_Burned, Height, Weight) VALUES (%s, %s, %s, %s, %s, %s)")

            data = (date1,workout1,duration1,calorie1,height1,weight1)
            try:
                #executing the sql command
                mycursor.execute(insert_stmt,data)
                #commit changes in database
                mydb.commit()
            except:
                mydb.rollback()
            message.set("Data Stored Successfully !!")

    def Clear():
        date.delete(0,'end')
        workout.delete(0,'end')
        duration.delete(0,'end')
        calorie.delete(0,'end')
        height.delete(0,'end')
        weight.delete(0,'end')
        message.set("Enter New Data !!")
    def Show():
        global Third
        Third = Toplevel(Second)
        Third.title("Contents of "+nuser.title()+"Table")
        Third.geometry("1240x700")
        Third.configure(background="floral white")

        #Defining Headings
        e=Label(Third,width=15,text='SrN.',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=0)
        e=Label(Third,width=15,text='Date',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=1)
        e=Label(Third,width=15,text='Workout',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=2)
        e=Label(Third,width=15,text='Duration',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=3)
        e=Label(Third,width=15,text='Calories_Burned',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=4)
        e=Label(Third,width=15,text='Height',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=5)
        e=Label(Third,width=15,text='Weight',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",15))
        e.grid(row=0,column=6)

        #Establishing Connection
        my_connect = mysql.connector.connect(
          host="localhost",
          user="root", 
          passwd="",
          database="fitnesslogbuddy"
        )

        my_conn = my_connect.cursor()
        user='user'
        #To Print Table
        my_conn.execute("SELECT * FROM "+nuser)
        i=1
        for element in my_conn: 
            for j in range(len(element)):
                e = Label(Third,width=18, text=element[j],borderwidth=5,relief='ridge',bg='grey86',fg="black",font=("Arial",11) ) 
                e.grid(row=i, column=j) 

            i=i+1

        Third.mainloop()

    #defining DataInput Window
    def datainputwin():
        global Second
        Second = Toplevel(First)
        #Setting title of screen
        Second.title("user "+nuser.title()+" Data Logger")
        #setting height, width and bg of screen
        Second.geometry("700x600")
        Second.configure(background="floral white")
        #declaring variable
        global  message;
        global date
        global workout
        global duration
        global calorie
        global height
        global weight
        date = StringVar()
        workout = StringVar()
        duration=StringVar()
        calorie=StringVar()
        height=DoubleVar()
        weight=DoubleVar()
        message=StringVar()
        #Creating layout of Data Logger

        #Top Message
        Label(Second,width="300", text="Please Enter Details Below", bg="orange",fg="black",font=("Calisto MT",25,"bold")).pack()

        #date Label
        Label(Second, text="Date (dd/mm/yyy) * ",bg="floral white",font=("Arial",15)).place(x=100,y=80)
        #date textbox
        date=Entry(Second, textvariable=date,width=22,bg="thistle1",font=("Arial",13))
        date.place(x=400,y=82)

        #workout Label
        Label(Second, text="Workout (focused muscle) * ",bg="floral white",font=("Arial",15)).place(x=100,y=120)
        #workout textbox
        workout=Entry(Second, textvariable=workout,width=22,bg="thistle1",font=("Arial",13))
        workout.place(x=400,y=122)

        # duration Label
        Label(Second, text="Duration (min) * ",bg="floral white",font=("Arial",15)).place(x=100, y=160)
        # duration textbox
        duration=Entry(Second, textvariable=duration,width=22,bg="thistle1",font=("Arial",13))
        duration.place(x=400, y=162)

        # calorie Lable
        Label(Second, text="Calorie_Burned * ",bg="floral white",font=("Arial",15)).place(x=100, y=200)
        # calorie textbox
        calorie=Entry(Second, textvariable=calorie,width=22,bg="thistle1",font=("Arial",13))
        calorie.place(x=400, y=202)

        # height Lable
        Label(Second, text="Height (cm) * ",bg="floral white",font=("Arial",15)).place(x=100, y=240)
        # height textbox
        height=Entry(Second, textvariable=height,width=22,bg="thistle1",font=("Arial",13))
        height.place(x=400, y=242)

        # weight Lable
        Label(Second, text="Weight (kg) * ",bg="floral white",font=("Arial",15)).place(x=100, y=280)
        # weight textbox
        weight=Entry(Second, textvariable=weight,width=22,bg="thistle1",font=("Arial",13))
        weight.place(x=400, y=282)

        #Label for displaying login status[success/failed]
        status=Label(Second, text="",textvariable=message,fg="medium blue",bg="floral white",font=(15))
        status.place(x=398,y=320)

        #Lable for Show Data
        Label(Second, text="Click 'Show Data' Button to View your Whole Data Till Now",bg="floral white",fg="VioletRed4",font=("Arial",15,"underline")).place(x=90, y=450)
        
        #Register button
        Button(Second, text="Register", width=10, height=1, bg="orange",activebackground="green yellow",font=("Arial",13),command=Input).place(x=400,y=360)

        #Clear Button
        Button(Second, text="Clear", width=6, height=1, bg="orange",activebackground="orange red",font=("Arial",13),command=Clear).place(x=517,y=360)

        #Show DataBase Button
        Button(Second, text="Show Data", width=10, height=1, bg="orange",activebackground="cornflower blue",font=("Arial",13),command=Show).place(x=300,y=500)

        Second.mainloop()

    #calling function DataInput Window
    datainputwin()


#importing connection with database
mydb = mysql.connector.connect( host='localhost',user='root', password='',database="fitnesslogbuddy")

#creating the FitnessLogBuddy main window.
First = Tk() 
First.title("Fitness Log Buddy")    #title of the main window.
First.geometry("1200x450") #size of main window.
First.configure(background="floral white")

#declaring variable
global UID
UID = StringVar()
#Welcoming Message
Label(First,text="We welcome you to our Application Fitness Log Buddy !!",width=300,bg="orange",fg="black",font=("Calisto MT",30,"bold")).pack()

#App Description
Label(First,text="Here you can Log your Daily Workout Data and Record them in your Personal Database,\nWhich Allows you to Access the Whole Data Whenever Needed.",bg="floral white",fg="dark slate gray",font=("Calisto MT",20,"bold")).place(x=50,y=80)

#To Login
Label(First,text= "Login through your User ID:",bg="floral white",fg="forest green",font=("Calisto MT",18)).place(x=100,y=200)
#Login Entry
login=Entry(First,textvariable=UID,width=30,bg="PaleTurquoise1",font=("Arial",18))
login.place(x=102,y=265)
#Message
Label(First,text="NOTE- (if you're a NEW USER then your new database will be created)",bg="floral white",fg="blue",font=("Arial",12,"italic")).place(x=100,y=350)
#Message
Label(First,text="*(underscores,alphabets and numeric data is allowed, not case sensitive)",bg="floral white",fg="red",font=("Arial",10,"italic")).place(x=100,y=300)

#Login Button
btn1 = Button(First,text ="Login",width=10,pady=5,bg="orange",activebackground="green yellow",command=open2win)
btn1.place(x=510,y=262)

#Our Intro
Label(First,text="Maded by:\n\t~Shlok Agarwal\n\t   ~Vishal Chauhan",bg="floral white",font=("Arial",12,"italic")).place(x=970,y=370)

First.mainloop()
