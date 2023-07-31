#____________________________________________________________________________________
#DAY 21

#_________________________________________________________________
#DECORATORS IN PYTHON

# eg one |
"""def decor(func):
    def inner_function(x,y):
        if x<0:
            x = 0
        if y<0:
            y = 0
        return func(x,y)
    return inner_function
def add(a,b):
    res= a+b
    return res
add = decor(add)
print(add(9,56))
print(add(-10,5))"""

#eg two | To Make factorial of any number
"""def decor(func):
    def inner_function(a):
        if a<0:
            print("Argument given",a,"is a negative argument")
           
        elif a==0:
            print("Factorial of",a,"is =",1)
            
        return func(a)
    return inner_function
    
def fact(x):
    fac=1
    for i in range (1,x+1):
        fac *=i
    return fac

fact=decor(fact)
n=int(input("Enter a number to find its factorial"))
print("Factorial of",n,"is =",fact(n))"""
            #or (using @decor)
"""def decor(func):
    def inner_function(a):
        if a<0:
            print("Argument given",a,"is a negative argument")
           
        elif a==0:
            print("Factorial of",a,"is =",1)
            
        return func(a)
    return inner_function
    
@decor
def fact(x):
    fac=1
    for i in range (1,x+1):
        fac *=i
    return fac

n=int(input("Enter a number to find its factorial"))
print("Factorial of",n,"is =",fact(n))"""

#_________________________________________________________________________________
#POLYMORPHISM IN PYTHON

#_____________________________________
#Types Of Polymorphism

#__________
# Duck Type | (Same Method Name of Different Class Accessed by a function using object as argument of different classes)

"""class Duck:
    def talk(self):
        print("Quack....Quack.....")

class Dog:
    def talk(self):
        print("Bhow....Bhow.....")

class Cat:
    def talk(self):
        print("Meow....Meow.....")"""



#___________________________________________________________________________
#OVERLOADING in Python

#_________________________
#Types of Overloading

#_________________
#Operator Overloading

#Working of Magic Operator (__add__)
"""class Book:
    def __init__(self,pages):
        self.pages=pages

b1=Book(100)
b2=Book(200)

print(type(b1))
print(type(b2))
print(type(b1.pages))
print(type(b2.pages))
print(b1.pages + b2.pages)
print((b1.pages).__add__(b2.pages))     #__add__(magic operator)"""
