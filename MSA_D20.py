#__________________________________________________________________________________________________________________
#DAY 2000

#______________________________________________________________________
# INHERITANCE IN PYTHON

#___________________________________________________
#Types Of INHERITANCE

#____________________
# Single Level Inheritance
"""class A:
    def m1(self):
        print("Class A m1 method")

class B(A):
    def m2(self):
        print("Child B is derived from A class. m2 Method")

obj=B()
obj.m1()
obj.m2()"""

#__________________
# MultiLevel Inheritance
"""class A:
    def m1(self):
        print("Class A m1 method")

class B(A):
    def m2(self):
        print("Child B is derived from A class. m2 Method")

class C(B):
    def m3(self):
        print("Child C is derived from B class. m3 Method")        

obj=C()
obj.m1()
obj.m2()
obj.m3()"""

#__________________
# Hierarichal Inheritance
"""class A:
    def display(self):
        print("Class A m1 method")

class B(A):
    def display(self):
        print("Child B is derived from A class. m2 Method")

class C(A):
    def display(self):
        print("Child C is derived from A class. m3 Method")        

c=C()
b=B()
c.display()
b.display()"""

#_________________
# Multiple Inheritance
"""class p1:
    def m1(self):
        print("Class parent1 m1 method")

class p2:
    def m2(self):
        print("Class parent2 m2 Method")

class C(p1,p2):
    def m3(self):
        print("Child C is derived from p1,p2 class. m3 Method")        

obj=C()
obj.m1()
obj.m2()
obj.m3()"""

#___________________________________________________________________________
#W.A.P to get marks and score of student then total it and display all (with multiple inheritance)
class Student:
    def get_marks(self):
        self.comp=int(input("Enter marks of Computer Subject:"))
        self.math=int(input("Enter marks of Maths Subject:"))
    def put_marks(self):
        print("Marks in Computer Subject is =",self.comp)
        print("Marks in Maths Subject is =",self.math)

class Sports:
    def get_score(self):
        self.sc=int(input("Enter Score gained in sports:"))
    def put_score(self):
        print("Score in Sports =",self.sc)

class Total(Student,Sports):
    def total(self):
        self.get_marks()
        self.get_score()
        self.total=self.comp + self.math + self.sc
    def display(self):
        self.put_marks()
        self.put_score()
        print("Total Marks =",self.total)

ob1=Total()
ob1.total()
ob1.display()
#____________________________________________________
#Constructor in Inheritance

# case one | calling parent constructor and all methods
"""class P1:
    def __init__(self):
        print("Default Constructor of Parent Class")
    def m1(self):
        print("Parent1 Method")

class Child(P1):
    def m2(self):
        print("Child Method")

c=Child()
c.m1()
c.m2()"""

# case two | calling child class constructor and all methods
"""class P1:
    def __init__(self):
        print("Default Constructor of Parent Class")
    def m1(self):
        print("Parent1 Method")

class Child(P1):
    def __init__(self):
        print("Default Constructor of Child Class")
    def m2(self):
        print("Child Method")

c=Child()
c.m1()
c.m2()"""

# case three | calling child class constructor and method
"""class P1:
    def __init__(self):
        print("Default Constructor of Parent Class")
    def m1(self):
        print("Parent1 Method")

class Child(P1):
    def __init__(self):
        print("Default Constructor of Child Class")
    def m1(self):
        print("Child Method")

c=Child()
c.m1()"""

# case four |calling parent and child class constructor and methods
"""class P1:
    def __init__(self):
        print("Default Constructor of Parent Class")
    def m1(self):
        print("Parent1 Method")

class Child(P1):
    def __init__(self):
        print("Default Constructor of Child Class")
        super().__init__()
    def m1(self):
        print("Child Method")
        super().m1()

c=Child()
c.m1()"""

