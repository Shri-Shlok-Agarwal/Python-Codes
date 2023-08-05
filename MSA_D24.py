#____________________________________________________________________________________
#DAY 22


#___________________________________________
#Overriding in Python

#__________________

#Constructor overriding   

"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Employee(Person):

    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def display(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal,"\n\n")

e1=Employee("Surabhi",16,3252,999999)
e1.display()
e2=Employee("Saurabh",21,41441,99900)
e2.display()"""



#____________________________________________________________________________________
#ABSTRACT CLASSES

# case one | correct (abstract class's abstract method is implemented in child class)
"""from abc import ABC, abstractmethod as am

#Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @am
    def intrest(self):
        "Abstract Class"
        pass

#sub class/ child class of abstract class
class SBI(Bank):
    def intrest(self):
        "Implementation of abstract method"
        print("In SBI Bank 5 %  Intrest Return")

s=SBI()
s.bank_info()
s.intrest()"""


# case two | error (abstract class's abstract method is not implemented in child class)
"""from abc import ABC, abstractmethod as am

#Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @am
    def intrest(self):
        "Abstract Class"
        pass

#sub class/ child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 9999")

s=SBI()
s.bank_info()
s.balance()"""


# case three | correction of case two (abstract class's abstract method is implemented in child class of a child class)
"""from abc import ABC, abstractmethod as am

#Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @am
    def intrest(self):
        "Abstract Class"
        pass

#sub class/ child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 9999")

class sub1(SBI):
    def intrest(self):
        "Implementation of abstract method"
        print("In SBI Bank 5 %  Intrest Return")

s=sub1()
s.bank_info()
s.balance()
s.intrest()"""

#NOTE:-  Concrete Methods can be defined in Abstract Classes.  (concrete methods =
#NOTE:-  An Abstract Class has more than one sub classes to implement different tasks.


# case four | correct (An Abstract Class has more than one sub classes to implement different tasks.)
"""from abc import ABC, abstractmethod as am

#Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @am
    def intrest(self):
        "Abstract Class"
        pass

#sub class/ child class of abstract class
class SBI(Bank):
    def intrest(self):
        "Implementation of abstract method"
        print("In SBI Bank 5 %  Intrest Return")

#sub class/ child class of abstract class
class HSBC(Bank):
    def intrest(self):
        "Implementation of abstract method"
        print("In HSBC Bank 12 %  Intrest Return")

s=SBI()
s.bank_info()
s.intrest()
h=HSBC()
h.bank_info()
h.intrest()"""


# case five | abstract class without inheriting ABC Class
"""from abc import *

class Demo:

    @abstractmethod
    def m(self):
        pass

    def n(self):
        print("Implemented Method")

t=Demo()
t.m()
t.n()"""
