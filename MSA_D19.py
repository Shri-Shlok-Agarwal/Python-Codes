#__________________________________________________________________________________________________________________#
#DAY 19

#___________________________________________
#W.A.P to Input Data initialize them and then print them

"""class Student:
    name,grade=None,None
    roll=0
    per=0.0
    def get_data(self,a,b,c,d):
        self.name=a
        self.grade=b
        self.roll=c
        self.per=d
        self.put_data()

    def put_data(self):
        print("\n\n\t*********STUDENT DETAILS*********\n\n")
        print("Student Name is =",self.name)
        print("Student Roll number is =",self.roll)
        print("Student Grade is =",self.grade)
        print("Student Percentage is =",self.per)

ob1=Student()
name=input("Enter Student Name:")
grade=input("Enter Student Grade:")
roll=int(input("Enter Student RollNo:"))
per=float(input("Enter Student Percentage:"))

ob1.get_data(name,grade,roll,per)"""
            #or (
"""class Student:
    name,grade=None,None
    roll=0
    per=0.0
    def get_data(self):
        self.name=input("Enter Student Name:")
        self.grade=input("Enter Student Grade:")
        self.roll=int(input("Enter Student RollNo:"))
        self.per=float(input("Enter Student Percentage:"))

    def put_data(self):
        self.get_data()
        print("\n\n\t*********STUDENT DETAILS*********\n\n")
        print("Student Name is =",self.name)
        print("Student Roll number is =",self.roll)
        print("Student Grade is =",self.grade)
        print("Student Percentage is =",self.per)

ob1=Student()
ob1.put_data()"""


#_______________________________________________________________________________
#CONSTRUCTORS

#______________________
#Basic Constructor Program
"""class Employee:
    def __init__(self):
        print("Constructor is executed automatically at the time of object creation",self)    #implicitly
emp=Employee()
emp.__init__()    #explicitly"""

#_______________________________________
#To Check The Availability of The Constructor init
"""class Sample:
    def m1(self):
        print("m1 is instance method called with object name")    #implicitly
s=Sample()
s.m1()
print(dir(Sample))"""

#____________________________________
#Constructor Types

#________________________
#Unparameterised Constructor

"""class employee:
    def __init__ (self):
        self.id=1
        print("Employee id is: ",self.id)
e1=employee()
e2=employee()
e3=employee()"""

#______________________
#Parameterized Constructor

"""class employee:
    
    def __init__ (self,id,name):
        self.id=id
        self.name=name
        
    def display(self):
        print("Employee id is: ",self.id,end="    ")
        print("Employee name is: ",self.name)
        
e1=employee(1,"Shlok")
e2=employee(2,"Vishal")
e1.display()
e2.display()"""


#_____________________________________________________
#W.A.P To Find Area Of Triangle Using Parameterized Constructor

"""class triangle:
    def __init__(self,base,height):
        self.area=0.5*base*height
        print ("Area of Triangle is =",self.area)
ob1=triangle(56,67)"""

        #or (user defined)

"""class triangle:
    def __init__(self,base,height):
        self.area=0.5*base*height
        print ("Area of Triangle is =",self.area)

n= int(input("Enter Base Of Triangle:"))
m= int(input("Enter Height Of Triangle:"))
ob1=triangle(n,m)"""










































































        #or (user de
