#______________________________________________________________________________________________
#DAY 10

#_________________________________
#Return MULTIPLE Values From Function
"""def m1(a,b):
    c=a+b
    d=a-b
    return c,d
x,y=m1(10,15)
print("Sum of a & b =",x)
print("Sub of a & b =",y)"""
        #or (user defined)
"""def m1(a,b):
    c=a+b
    d=a-b
    return c,d
n=int(input("Enter a number1: "))
m=int(input("Enter a number2: "))
x,y=m1(n,m)
print("Sum of a & b =",x)
print("Sub of a & b =",y)"""

#______________________________
#Function Calling ANOTHER Function
#eg one | ()
"""def m1():
    print("Method one")
def m2():
    print("Method two")
    m1()     #funtion calling another function
m2()"""

#eg two | (to take input in first function and calling it from second function and also do calculation in second function)
       #(operation calling calculator)
"""def calculator():
    n=int(input("Enter number 1: "))
    m=int(input("Enter number 2: "))
    return n,m
def operation():
    a,b=calculator()     #funtion calling another function
    c=a+b
    d=a-b
    return c,d
x,y=operation()
print("Sum of n & m =",x)
print("Sub of n & m =",y)"""

        #or (calculator calling operation)

"""def calculator():
    n=int(input("Enter number 1: "))
    m=int(input("Enter number 2: "))
    operation(n,m)  #funtion calling another function
def operation(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print("Sum of", a,"&",b,"=",c)
    print("Sub of", a,"&",b,"=",d)
    print("Mul of", a,"&",b,"=",e)
    print("Div of", a,"&",b,"=",f)
calculator()"""

#________________________________________________________________________________________
#FUNCTION ARE FIRST CLASS OBJECT
#_______________________
#Assigning Function to Variable
"""def add():
    print("We Assigned function to variable")
addition=add     #assining function to variable
addition()          #calling variable func"""

#______________________________________
#Pass Function a Parameter to Another Function
"""def display(x):
    print("This is Display Function")
def message():
    print("This is Message Function")
display(message())"""

#_________________________________________
#Define One Function In Another Function In Python
"""def first():
    print("This is Outer Function")
    def second():
        print("This is inner Function")
    second()
first()     #calling outer function
#second()    (error)"""
