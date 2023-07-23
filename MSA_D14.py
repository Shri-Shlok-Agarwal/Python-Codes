#______________________________________________________________________________
#DAY 14

#___________________________________________________________
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

#__________________________________________________________________
#LIST DATA TYPES

#____________________
#Creating an empty List
"""l1=[]
print(l1)
print(type(l1))"""

#___________________________
#Creating a List with ELEMENTS
"""names= ["rana","shlok","vishal",10,20,True,None]
print(names)"""

#____________________________
#Creating a List using list() function
"""r=range(0,10)
l=list(r)
print(l)
print(type(l))"""

#______________
#Mutability in List
"""l=[1,2,3,4,5]
print(l)
print("Before Modifying l[0]: ",l[0])
l[0]=20
print("After Modifying l[0]: ",l[0])"""

#______________________________
#Accessing List in PYTHON

#______________
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

#____________________
#By using Slicing Operator

"""n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])"""

#_____________
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

#_____________________
#FUNCTIONS of List

#
#Length Method (len())
"""n=[100,200,300,400,500,600]
print(len(n))"""

#
#Count Method (count())
"""n=[1,2,3,4,5,6,3,42,6,1,46,6,3,5,5,5,3,5,2,2,4]
print(n.count(5))
print(n.count(2))
print(n.count(6))"""

#
#Append Method (list.append())
"""l=[]
l.append("Vivek")
l.append("Paisa")
l.append("Dega")
print(l)"""

#
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

#
#Extend Method (list1.extend(list2))
"""l1=[1,2,3]
l2=['vivek','paisa','dega']
print("Before extend l1 is: ",l1)
print("Before extend l2 is: ",l2)
l2.extend(l1)
print("After extend l1 is: ",l1)
print("After extend l2 is: ",l2)"""


#
#Remove Method ( list.remove(element))
# one | 
"""l=[1,2,3]
l.remove(1)
print(l)"""

# two |
"""l=[1,2,3,1]
l.remove(1)
print(l)"""

# three |
"""l=[1,2,3]
l.remove(10)
print(l)"""

#
#Pop Method (list.pop(element))
"""l=[1,2,3,4,5]
print(l.pop(3))
print(l)
print(l.pop())
print(l)
print(l.pop(10))"""
