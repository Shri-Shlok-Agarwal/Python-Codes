#___________________________________________________________________________________________
#DAY 12 (H.W)

#____________________________________________________
#To Check If Any given Number is ARMSTRONG or NOT (H.W)
"""def count(n):
    if n==0:
        c=0
    else:
        c=1+count(n//10)
    return c

def armstrong(n,cnt):
    r=n%10
    if n==0:
        result=0
    else:
        result=(r**cnt)+ armstrong(n//10,cnt)
    return result
n=int(input("Enter a number to find its armstrong: "))
x=count(n)
print(x)
y=armstrong(n,x)
if y==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")"""

                #or (by sir)
"""def armstrong(num,n,count,t):
    if t==0:
        if count==num:
            return True
        else:
            return False
    digit = t%10
    count = count + digit**n
    t = t//10
    return armstrong(num,n,count,t)
num = int(input("Enter a number: "))
count = 0
n=len(str(num))
t=num
result = armstrong(num, n, count, t)

if result:
          print(num,"is an Armstrong number")
else:
          print(num,"is not an Armstrong number")"""

#___________________________________________________
#To Check If Any given Number is PALINDROME or NOT (H.W)
"""def count(n):
    if n==0:
        c=0
    else:
        c=1+count(n//10)
    return c

def palindrome(n):
    r=n%10
    cnt=count(n)
    a=10**(cnt-1)
    if n==0:
        result=0
    else:
        result=(r*a)+ palindrome(n//10)
    return result
n=int(input("Enter a number to find its armstrong: "))
y=palindrome(n)
print(y)
if y==n:
    print(n,"is an palindrome number")
else:
    print(n,"is not an palindrome number")"""
   

