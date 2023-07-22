#____________________________________________________________________________
#DAY 12

#_______________________________________________________________________________
#RECURSIVe AND LAMDA FUNCTIONS

#_________________________________________________________
#Recursive Functions (function calling itself)

#eg one | to print factorial of a number
"""def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
x=fact(5)
print("factorial = ",x)"""
        #or (user defined)
"""def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
n=int(input("Enter a number to show its Factorial: "))
x=fact(n)
print("factorial of",n,"is = ",x)"""

#eg two | Sum of digits using recursion
"""def add(n):
    r=n%10
    if n==0:
        result=0
    else:
        result=r+add(n//10)
    return result
x=add(123)
print("Sum of digits =",x)"""
        #or (user defined)
"""def add(n):
    r=n%10
    if n==0:
        result=0
    else:
        result=r+add(n//10)
    return result
n=int(input("Enter a number to show sum of its digits: "))
x=add(n)
print("Sum of digits of",n,"is = ",x)"""

#eg three | To check if any digit number is Armstrong or not (to be done)
def add(n,c):
    r=n%10
    if n==0:
        result=0
    else:
        result=(r**c)+add(n//10)
    return result
def count(n):
    c=0
    if n==0:
        c=0
    else:
        c=c+1
        n=n//10
    return c
n=int(input("Enter a number to show sum of its digits: "))
a=n
cnt=count(n)
x=add(n,cnt)
if x==n:
    print(a,"is an Armstrong number")
else:
    print(a,"is not an Armstrong number")

#eg four | To check if number is Palindrom or not (to be done)
def add(n):
    r=n%10
    if n==0:
        result=0
    else:
        result=(r*10)+add(n//10)
    return result
n=int(input("Enter a number to show sum of its digits: "))
x=add(n)
if x==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")

#_________________________________________________________
#LAMBDA Functions (Annomynus)

#eg one | square of a number
"""s=lambda a:a*a
x=s(4)
print(x)"""

#eg two | sum of two numbers
"""add = lambda a,b:a+b
x=add(4,5)
print("Sum =",x)"""

#_______________________________________________
#filter() function in lambda functions [filter(lambda,sequence)] (if item matches the operation then it filter it from sequence)

#eg one | get thousands
"""item_cost=[999,888,1100,1200,1300,777]
gt_thousand=filter(lambda x:x>=1000,item_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)"""

#________________________________________________
#map() function in lambda functions [map(lambda,sequence)] (create new list with operation on all items)
#eg one | 
""""without_gst_cost=[100,200,300,400]
with_gst_cost=map(lambda x: x+10,without_gst_cost)
x=list(with_gst_cost)
print("without GST items cost ",without_gst_cost)
print("with GST items cost ",x)"""

#____________________________________________________
#reduce() function in lambda functions [reduce(lambda,sequence)] (reduce the elements in single element by applying any specific condition or operation)
#eg one |
"""from functools import reduce
each_tem_costs = [111,222,333,444]
total_cost = reduce(lambda x,y: x+y, each_tem_costs)
print(total_cost)"""
