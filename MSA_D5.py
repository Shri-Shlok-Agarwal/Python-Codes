#To print Fibonaci Series using While loop
#"""x=0 | n=int(input("Enter the no. ofterms for fibonaci series: ")) | y=1 | i=1 | while(i<=n): |       print(x) |       z=x+y |       x=y |       y=z |       i+=1 |         #or | n=int(input("Enter the no. ofterms for fibonaci series: ")) | a=-1 | b=1 | x=1 | while(x<=n): |     z=a+b |     print(z) |     a=b |     b=z |     x+=1"""

#To find if the number is Prime or Not
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


#To print prime the numbers upto n term(not correct)
"""n=int(input("Enter the nth term"))

x=1
i=1
while i<=n:
    c=0
    while x<=i:
        if i%x==0:
            c+=1
        x+=1
    if c==2:
        print(i,"is a prime number")
    i+=1"""

#FOR LOOP

#Using for loop and extracting elements from list or string
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

#Using for loop with Range Function
"""for i in range (0,11):
    print(i)"""
#using for loop to print fibonaci series
"""n=int(input("Enter the no. of terms for fibonaci series: "))
a=0
b=1
for i in range(0,n+1):
    c=a+b
    print(c)
    a=b
    b=c"""

#To find if the number is Prime or Not
"""n=int(input("Enter the no. to check if it isprimeor not: "))
c=0
for i in range (1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")"""

#To print factorial of a number
"""n=int(input("Enter a Number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is= ",fact)"""

#to be done
"""n=int(input("Enter the nth term"))
c=0
for i in range(1,n+1):
    for j in range(1,i+1):"""
        

    


    



    
      
