#_______________________________________________________________________________________________________________________________________________________________
#DAY 14

#_____________________________________________________________________________________________________
#Working On Temperature Module

#Basic
"""import temperature
print(temperature.to_celcius(56))
print(temperature.to_fahren(56))
print(temperature.freezing_c)
print(temperature.freezing_f)"""

#To alias module
"""import temperature as temp
print(temp.to_celcius(56))
print(temp.to_fahren(56))
print(temp.freezing_c)
print(temp.freezing_f)"""

#To use from and import all(*)
"""from temperature import *
print(to_celcius(56))
print(to_fahren(56))
print(freezing_c)
print(freezing_f)"""

#To use from , import members and give them alias and calling imported only
"""from temperature import to_celcius as cel, to_fahren as frn
print(cel(56))
print(frn(56))"""

#To use from , import members and give them alias but call all members
"""from temperature import to_celcius as cel, to_fahren as frn
print(cel(56))
print(frn(56))
print(freezing_c)   #error
print(freezing_f)   #error"""

#_______________________________________________________________________________________________________________________________________________________________________
#LIST DATA TYPE

#___________________________________________________________________________
# LIST BASICS

#______________________
#Creating an empty List
"""l1=[]
print(l1)
print(type(l1))"""

#_____________________________
#Creating a List with ELEMENTS
"""names= ["rana","shlok","vishal",10,20,True,None]
print(names)"""

#_____________________________________
#Creating a List using list() function
"""r=range(0,10)
l=list(r)
print(l)
print(type(l))"""

#__________________
#Mutability in List
"""l=[1,2,3,4,5]
print(l)
print("Before Modifying l[0]: ",l[0])
l[0]=20
print("After Modifying l[0]: ",l[0])"""

#_________________________________________________________
#Accessing List in PYTHON

#_________________
#By using Indexing

"""names=["rana","shlok","vishal"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[10])     #out of range error
print(type(names))
print(type(names[0]))
print(type(names[1]))
print(type(names[2]))"""

#_________________________
#By using Slicing Operator

"""n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])"""

#_______________
#By Using Loops

#one | using for      
"""n=[100,200,300,400,500,600]
for x in n:
    print(x)"""


#two | using while
"""n=[100,200,300,400,500,600]
x=0
while x<len(n):
    print(n[x])
    x+=1"""

#_______________________________________________________________________________
# Methods of List in Python

#_____________________
#Length Method (len())
"""n=[100,200,300,400,500,600]
print(len(n))"""

#______________________
#Count Method (count())
"""n=[1,2,3,4,5,6,3,42,6,1,46,6,3,5,5,5,3,5,2,2,4]
print(n.count(5))
print(n.count(2))
print(n.count(6))"""

#_____________________________
#Append Method (list.append())
"""l=[]
l.append("Vivek")
l.append("Paisa")
l.append("Dega")
print(l)"""

#__________________________________________
#Insert Method (list.insert(index,element))
"""l=[10,20,30,40]
print(l)
l.insert(1,111)
print(l)
l.insert(-1,222)
print(l)
l.insert(10,333)
print(l)
l.insert(-10,444)
print(l)"""

#___________________________________
#Extend Method (list1.extend(list2))
"""l1=[1,2,3]
l2=['vivek','paisa','dega']
print("Before extend l1 is: ",l1)
print("Before extend l2 is: ",l2)
l2.extend(l1)
print("After extend l1 is: ",l1)
print("After extend l2 is: ",l2)"""


#_____________________________________
#Remove Method ( list.remove(element))
# eg one | 
"""l=[1,2,3]
l.remove(1)
print(l)"""

# eg two |
"""l=[1,2,3,1]
l.remove(1)
print(l)"""

# eg three |
"""l=[1,2,3]
l.remove(10)
print(l)"""

#______________________________
#Pop Method (list.pop(element))
"""l=[1,2,3,4,5]
print(l.pop(3))
print(l)
print(l.pop())
print(l)
print(l.pop(10))"""

#_______________________________
#Reverse method (list.reverse())
"""n=[1, 2, 3, 4, 'two']
print(n)
n.reverse()
print(n)"""

#_________________________
#Sort method (list.sort())

#eg one | (correct and only sort list of same data type elements)
"""n=[1, 4, 5, 2, 3]
n.sort()
print(n)
s=['Suresh', 'Ramesh', 'Arjun']
s.sort()
print(s)"""

#eg two | (give error as elements are not of same data type)
"""n=[1, 4, 5, 2, 3, 'Suresh', 'Ramesh', 'Arjun']
n.sort()
print(n)"""


#_________________________________________________________________________________________________________________
# LIST ALIASING and CLONING

#____________________________________
# Aliasing List in Python (dependent)

"""x=[10, 20, 30,40,50]
y=x
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))
y[3] = 100
print(x)
print(y)
print(id(x))
print(id(y))"""

#________________________________________
# Cloning in List in Python (independent)

#______________________________
#Cloning using slicing operator
"""x=[10, 20, 30,40,50]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))
y[0] = 100
print(x)
print(y)
print(id(x))
print(id(y))"""

#__________________________________________
#Cloning by using Copy method (list.copy())
"""x=[10, 20, 30]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))"""

#_________________________________________________________________________________________________________________
#MATHEMATICAL OPERATORS on LIST

#______________________
# Concatenation of List
"""a= [1, 2, 3]
b= [4, 5, 6]
c = a + b
print(c)"""

#________________________________
# Multiplication operator on List
"""a = [1, 2, 3]
print(a)
print(2*a)"""

#_____________________________
#COMPARISON of LISTS in Python

#comparing lists of numbers
"""print([1, 2, 3] < [2, 2, 3])
print([1, 2, 3] < [1, 2, 3])
print([1, 2, 3] <= [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])
print([1, 2, 3] < [0, 2, 3])
print([1, 2, 3] <= [3, 2, 1])
print([1, 2, 3] == [1, 2, 3])"""

#comparing lists of strings
"""x =["abc", "def", "ghi"]
y =["abc", "def", "ghi"]
z =["ABC", "DEF", "GHI"]
a =["abc", "def", "ghi", "jkl"]
print(x==y)
print(x==z)
print(x<=a)
print(x>y)
print(x==z)
print(x==a)"""

#___________________________
#MEMBERSHIP Operator in List
"""x=[10, 20, 30, 40, 50]
print(20 in x) # True
print(20 not in x) # False
print(90 in x) # False
print(90 not in x) # True"""

#________________________________________________
# NESTED LISTS 
"""a = [80, 90]
b = [10, 20, 30, a]
print(b)
print(b[0])
print(b[1])
print(b[2])
print(b[3])"""

#____________________________________________________________________________________________________________
#LIST COMPREHENSIONS IN PYTHON

#___________________
#Multiplying with 2
"""x = [1, 2, 3, 4]
y = []
for i in x:
    y.append(i*2)
print(y)"""

#The above code can be written in a single line using list comprehensions.

#_____________________________________________________________________________
#List Comprehensions (list = [expression for item1 in iterable1 if statement])

# type one |
"""x = [1, 2, 3, 4]
y = [ i*2 for i in x]
print(y)"""

# type two |
"""s=range(1, 20, 3)
for i in s: #This loop is for knowing what is in s
    print(i)
m=[x for x in s if x%2==0] #List comprehension
print(m)"""
