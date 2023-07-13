#Use of nested if
#"""a=int(input("Enter number for a")) | b=int(input("Enter number for b")) | c=int(input("Enter number for c")) | if a>b: |     if a>c: |         print("a is the greatest number",a) |     else: |         print("c is the greatest number",c) | else: |     if b>c: |         print("b is the greatest number",b) |     else: |         print("c is the greatest number",c)"""

#WAP to make a arithematic calculator
#"""n1=int(input("Enter number one: ")) | n2=int(input("Enter number two: ")) | ao=input("Enter the Arithmatic Operation to be used: ") | if (ao=="+"): |     print("Sum of",n1,"and",n2,"is = ",n1+n2) | elif (ao=="-"): |     print("Subtraction of",n1,"and",n2,"is = ",n1-n2) | elif (ao=="*"): |     print("Multiplication of",n1,"and",n2,"is = ",n1*n2) | elif (ao=="/"): |     print("Division of",n1,"and",n2,"is = ",n1/n2) | elif (ao=="%"): |     print("Modulus of",n1,"and",n2,"is = ",n1%n2) | elif (ao=="//"): |     print("Floor Division of",n1,"and",n2,"is = ",n1//n2) | else: |     print("You entered invalid Arithmatic Operation ",ao)"""     

#LOOPING STATEMENTS

#using while loop
"""#eg one to print no. upto 10
x=1
while (x<=10):
    print(x)
    x+=1
print("\nEND")"""

#eg two to print even no.s in between of n terms
"""n1=int(input("Enter n1 term: "))
n2=int(input("Enter n2 term: "))
x=n1
while(x>=n1 and x<=n2):
    if (x%2==0):
        print(x)
    x+=1
print("END")"""

#eg three to print table of 2
"""x=1
t=
while (x<=10):
    print(x,"*",t,"=",x*t)
    x+=1"""

#eg four | to print factorial of n term
n=int(input("Enter number to print its factoria: "))
x=1
fact=1
while (x<=n):
    fact=(fact*x)
    x+=1
print("factorial of",n,"is =",fact)
           #or
n=int(input("Enter number to print its factoria: "))
fact=1
while (n>0):
    fact=(fact*n)
    n-=1
print("factorial of",n,"is =",fact)
           #or
n=int(input("Enter number to print its factoria: "))
x=n
fact=1
while (x>=1):
    fact=(fact*x)
    x-=1
print("factorial of",n,"is =",fact)
