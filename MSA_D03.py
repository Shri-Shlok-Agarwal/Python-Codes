#_______________________________________________________________________________________________________________________________________________________________________
#DAY 03

#3 |___________________________________________________________________________________________________________________
#INPUT FUNCTION

#3.1 |________________
#Use of input function
"""name=input('Enter your Name: ')
print('Name is: ',name)
print(type(name))"""

#3.2.1 |_________________________________
#Use of input to input number (wrong way)
"""rollno=input('Enter your roll no: ')
print('rollno is: ',rollno)
print(type(rollno))""""

#3.2.2 |________________________________
#Use of input to input no.s (wrong way).
"""a=input('Enter no a :')
b=input('Enter no a : ')
print('value in a is: ',a)
print('value in b is: ',b)
print(type(a))
print(type(b))"""

#3.2.3 |_______________________________________________
#Use of input to input no.s and to add them (wrong way).
"""a=input('Enter no a : ')
b=input('Enter no a : ')
print('value in a is: ',a)
print('value in b is: ',b)
print('Sum of a and b: ',(a+b))
print(type(a))
print(type(b))"""

#3.2.4 |______________________________________________________
#Use of input to input no.s and to add them (still wrong way).
"""a=input('Enter no a : ')
b=input('Enter no a : ')
print('value in a is: ',int(a))
print('value in b is: ',int(b))
print('Sum of a and b: ',int(a)+int(b))
print(type(a))
print(type(b))"""

#3.2.5 |___________________________________________________
#Use of input to input no.s and to add them (correct way).
"""a=int(input('Enter no a : '))
b=int(input('Enter no a : '))
print('value in a is: ',a)
print('value in b is: ',b)
print('Sum of a and b: ',(a+b))
print(type(a))
print(type(b))"""

#4 |___________________________________________________________________________________________________________________________________
#CONTROL STATEMENTS

#4.1 |________
#if Statement
"""num=int(input("enter a no.: "))
if (num%2==0):
    print(num," is an even number")"""
#4.2 |______________
#if else statements
"""age=int(input("Enter age: "))
if (age>=18):
        print("You are eligibe")
else:
        print("you are not eligibe")"""

"""#another eg"""
"""num=int(input("Enter Number: "))
if (num>0):
        print("No. is Positive")
else:
        print("No. is Negative")"""

        #another eg
"""num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
if (num1>num2):
        print("Number ",num1," is greater")
else:
        print("Number ",num2," is greater")"""

#4.3 |___________________
#if elif else statements
"""num=int(input("Enter Number: "))

if (num<=10):
        print("Number ",num," is less or equal to 10")
elif(num<=50):
        print("Number ",num," is less or equal to 50")
elif(num<=100):
        print("Number ",num," is less or equal to 100")
else:
    print("Number ",num,"is neither less nor equal to 10,50,100")"""
