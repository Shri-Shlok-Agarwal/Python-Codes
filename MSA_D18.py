#__________________________________________________________________________________________________________________#
#DAY 18

#________________________________________________________________________________
#INTODUCTION TO OOPS

#_________________________
#Making a Class With Variables
"""class Demo:
    name="SHLOK"
    roll=66

ob1=Demo()
print("Name is =",ob1.name)
print("Roll number is =",ob1.roll)"""

            #or (user defined)

"""class Demo:
    name=input("Enter Your Name")
    roll=int(input("Enter Roll Number"))

ob1=Demo()
print("Name is =",ob1.name)
print("Roll number is =",ob1.roll)"""

                #or (by sir)

"""class Demo:
    name,grade=None,None
    roll=0
    per=0.0

ob1=Demo()
ob1.name=input("Enter Student Name:")
ob1.grade=input("Enter Student Grade:")
ob1.roll=int(input("Enter Student RollNo.:"))
ob1.per=float(input("Enter Student Percentage: "))
print("\n\n\t***************STUDENT DETAILS**************\n\n")
print("Student Name is =",ob1.name)
print("Student Roll number is =",ob1.roll)
print("Student Grade is =",ob1.grade)
   print("Student Percentage is =",ob1.per)"""

#_______________________
#Making Class With Methods
"""class Demo:
    def display(self):
        print("This is a display method inside class Demo",self)
obj=Demo()
obj.display()
ob1=Demo()
ob1.display()"""

#___________________________________________
#W.A.P to Input Data initialize them and then print them

"""class student():
    name,grade=None,None
    roll=0
    per=0.0
    def get_data(self):
        self.name=input("Enter Student Name:")
        self.grade=input("Enter Student Grade:")
        self.roll=int(input("Enter Student RollNo:"))
        self.per=float(input("Enter Student Percentage:"))

    def put_data(self):
        print("\n\n\t*********STUDENT DETAILS*********\n\n")
        print("Student Name is =",self.name)
        print("Student Roll number is =",self.roll)
        print("Student Grade is =",self.grade)
        print("Student Percentage is =",self.per)

ob1=student()
ob1.get_data()
ob1.put_data()"""

        #or (argument type)
"""class Student():
    name,grade=None,None
    roll=0
    per=0.0
    def get_data(self,a,b,c,d):
        self.name=a
        self.grade=b
        self.roll=c
        self.per=d

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

ob1.get_data(name,grade,roll,per)
ob1.put_data()"""
