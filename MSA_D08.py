#_____________________________________________________________________________________________________________________________________________________
#DAY 08

#6.11 |________________________________________________________________________________________________
#PREDEFINED METHOD TO REMOVE SPACES FROM STRING

#6.11.1 |______________________________________________________________
#Use Of STRIP Function(remove spaces from start and end of the string)
"""course=" Python "
print("with spaces course lenth is: ",len(course))
x=course.strip()
print("after removing spaces course lenth is: ",len(x))"""

#6.11.2 |______________________________________________________
#Use Of LSTRIP Function(remove spaces from left of the string)
"""course=" Python"
print("with spaces course lenth is: ",len(course))
x=course.lstrip()
print("after removing spaces course lenth is: ",len(x))"""

#6.11.3 |_______________________________________________________ 
#Use Of RSTRIP Function(remove spaces from right of the string)
"""course=" Python "
print("with spaces course lenth is: ",len(course))
x=course.rstrip()
print("after removing spaces course lenth is: ",len(x))"""

#6.12 |_______________________________________________________________________________________________
#TO FIND SUBSTRING IN A STRING (find,index,rfind,rindex)

#6.12.1 |_____________________________________
#FORWARD Finding(find,index)

#6.12.1.1 |___________
#Use Of Find Function
"""course="Python Programming Language"
print(course.find("g"))
print(course.find("o",5,))
print(course.find("zee",5,))#(if substring is not found then it will give -1 as result)"""

#6.12.1.2 |____________
#Use Of Index Function
"""course="Python Programming Language"
print(course.index("Programming"))
print(course.index("hello"))#error(if substring is not found then it will give ValueError)"""

#6.12.1.3 |_________
#Handling the ERROR
"""s="Python Programming Language"
try:
    print(s.index("hello"))
except ValueError:
    print("Not Found")"""

#6.12.2 |_____________________________________
#BACKWARD Finding(rfind,rindex)

#6.12.2.1 |___________
#Use Of RFind Function
"""course="Python Programming Language"
print(course.rfind("g"))
print(course.rfind("o",5,))
print(course.rfind("zee",5,))#(if substring is not found then it will give -1 as result)"""

#6.12.2.2 |____________
#Use Of RIndex Function
"""course="Python Programming Language"
print(course.rindex("Programming"))
print(course.rindex("hello"))#error(if substring is not found then it will give ValueError)"""

#6.13 |_____________________________________________________________________________________________________
#Use Of COUNT Function(it count the number of accurance of the substring)
"""course="Python Programming Language"
print(course.count("Programming"))
print(course.count("a"))"""

#6.14 |______________________________________________________________________________________________________
#TO REPLACE A STRING WITH ANOTHER STRING WITH HELP OF REPLACE FUNCTION
"""s1="Python Programming Language"
s2=s1.replace("Python","Java")
print(s1)
print(s2)
print(id(s1))
print(id(s2))"""

#6.15 |______________________________________________________________________________________________________
#SPLITING A STRING IN PYTHON

#6.15.1 |_________
#type 1
"""message="Python Programming Language"
a=message.split()
print("Before Splitting: ",message)
print("After Splitting: ",a)
print(type(message))
print(type(a))
for x in a:
      print(x)"""
#6.15.2 |__________
#type 2
"""message="Python Programming Language,it is easy,undarstandable, and good"
a=message.split(",")
print("Before Splitting: ",message)
print("After Splitting: ",a)"""


#6.16 |_______________________________________________________________________________________________________________
#TO JOIN TWO STRINGS (join two strings with given seperator symbol)

#6.16.1 |________________________________________________________
#Seperato is '-' symbol joining strings by using JOIN() METHOD
"""profile=["Roshan","Actor","Bhartiya"]
candidate='-'.join(profile)
print(profile)
print(candidate)
print(type(profile))
print(type(candidate))"""

#6.16.2 |_________________________________________________________
#Seperato is ': ' symbol joining strings by using JOIN() METHOD
"""profile=["Roshan","Actor","Bhartiya"]
candidate=': '.join(profile)
print(profile)
print(candidate)
print(type(profile))
print(type(candidate))"""

#6.17 |_________________________________________________________________________________________
#CHANGE CASE OF STRING IN PYTHON (upper,lower,swapcase,title,capitalize)
"""message="Python Programming Language,it is easy"
print(message.upper())
print(message.lower())
print(message.swapcase())
print(message.title())
print(message.capitalize())"""

#6.18 |__________________________________________________________________________________________________
#FORMATING STRINGS (it sets priority)
"""name="Rakesh"
salary=100
age=20
print("{} 's salary is {} and his age is {}".format(name,salary,age))
print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
print("{x} 's salary is {y} and his age is {z}".format(y=age,z=salary,x=name))"""

#6.19 |___________________________________________________________________________________________________
#CHARACTER DATA TYPE (always shows as string)
"""gender1="M"
gender2="F"
print(gender1)
print(gender2)
print(type(gender1))
print(type(gender2))"""
