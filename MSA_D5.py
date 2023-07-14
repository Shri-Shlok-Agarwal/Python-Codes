#eg five | To print Fibonaci Series using While loop
"""x=0
n=int(input("Enter the no. ofterms for fibonaci series: "))
y=1
i=1
while(i<=n):
    print(x)
    z=x+y
    x=y
    y=z
    i+=1
        #or
n=int(input("Enter the no. ofterms for fibonaci series: "))
a=-1
b=1
x=1
while(x<=n):
    z=a+b
    print(z)
    a=b
    b=z
    x+=1"""

#eg six | To find if the number is Prime or Not
"""n=int(input("Enter the no. to check if it isprimeor not: "))
c=0
x=1
while x<=n:
    if n%x==0:
        c+=1
    x+=1
if c==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")"""


#______________
#For Loop(for)
#eg one | Using for loop and extracting elements from list or string
"""
'''eg1'''
x=[10,20,30,"vivek","shlok","yash"]
for i in x:
    print(i,end=' ')

'''eg2'''
x="Shlok Agarwal" 
for i in x:
    print(i,end=' ')		
"""

#eg two | Using for loop with Range Function
"""for i in range (0,11):
    print(i)"""
#eg three | using for loop to print fibonaci series
"""n=int(input("Enter the no. of terms for fibonaci series: "))
a=0
b=1
for i in range(0,n+1):
    c=a+b
    print(c)
    a=b
    b=c"""

#eg four | To find if the number is Prime or Not
"""n=int(input("Enter the no. to check if it isprimeor not: "))
c=0
for i in range (1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")"""

#eg five | To print factorial of a number
"""n=int(input("Enter a Number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is= ",fact)"""

#eg six | To Print Prime Numbers between 1 and n'th term
"""n=int(input("Enter the nth term"))

for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if (i%j==0):
            c+=1
    if (c==2):
        print(i,end="\t")""" 
