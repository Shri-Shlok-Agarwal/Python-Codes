#_______________________________________________________________________________________________________________
#DAY_09

#_______________________________________________________________________
#PYTHON FUNCTIONS

#_________________________
#Function with no arguments
"""def display(): #defining function
    print("My first function")
display()
display() #calling of function
display()"""

#________________________________________________
#Define a function and call it with a different name (error)
"""def one():
    print("hello")
two()"""

#_________________________________________
#Function with Parameters/arguments in Python
#(function performing additions of two numbers)
"""def add(a,b):
    print("Sum of two values: ",(a+b))
add(4,5)"""
    #or (user defined in same)
"""def add(a,b):
    c=a+b
    print("Sum of",a,"and",b,"is = ",c) 
n=int(input("Enter value of a: "))
m=int(input("Enter value of b: "))
add(n,m)"""

#Function performing additions of two numbers in loop
"""def add(a,b):
    c=a+b
    print("Sum of",a,"and",b,"is = ",c) 
for i in range(1,6):
    n=int(input("Enter value of a: "))
    m=int(input("Enter value of b: "))
    add(n,m)"""

#____________________________________________
#W.A.Function to check if the number is even or not
"""def check(a):
    if (a%2==0):
        print(a,"is an even number")
    else:
        print(a,"is not an even number")
n=int(input("Enter value of a: "))
check(n)"""

#________________________________
#Use Of RETURN Keyword in Python
"""def add(a,b):
    c=a+b
    return c
n=int(input("Enter value of a: "))
m=int(input("Enter value of b: "))
x=add(n,m)
print("Sum of",n,"and",m,"is = ",x)"""

#__________________________________________
#W.A.Function to print FACTORIAL of n numbers
"""def factorial(a):
    x=1
    flag=1
    while (x<=a):#(using while)
        flag=flag*x
        x+=1
    return flag
n=int(input("Enter range: "))
for i in range(n):
    m=int(input("Enter value to find its factorial: "))
    fact=factorial(m)
    print("Factorial of",m,"is = ",fact)"""
    #or(using for)
"""def factorial(a):
    flag=1
    for i in range(1,a+1):
        flag=flag*i
    return flag
n=int(input("Enter range: "))
for i in range(n):
    m=int(input("Enter value to find its factorial: "))
    fact=factorial(m)
    print("Factorial of",m,"is = ",fact)"""
