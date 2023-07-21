#_________________________________________________________________________________________________________
#DAY 07

#6 |_____________________________________________________________
#USING STRINGS

#6.1 |____________
#Multiline string
"""a='''My name is shlok"
b=my friend name is yash'
c=he is wearing pink'''
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))"""

#6.2 |_________
#Empty String
"""a=""
print(a)
print(type(a))"""

#6.3 |____________________
#ACCESSING USING INDEXING
#Accessing a string with indexes in python
"""A="Hello world"
print(A[0])
print(A[3])"""

#6.3.1 |___________
#Accessing a string with indexes and range(slicing)
"""A="Hello world"
print(A[1:6:1])
print(A[4])"""

#6.3.2 |___________
#Accessing a string with out of bond indexes
"""A="Hello world"
print(A[0])
print(A[300])"""

#6.3.3 |___________
#Accessing a string with negative indexes
"""A="Hello world"
print(A[-7])
print(A[-4])"""

#6.3.4 |___________
#Accessing a string with negative indexes and range(slicing)
"""A="Hello world"
print(A[-1:-6:-1])
print(A[-4])"""

#6.extras |______________
#Print caracter by caracter by caracter using for loop
"""A="Hello world"
for a in A:
    print(a)"""

#6.4 |____________________
#ACCESSING USING SLICING

#6.4.1 |_____________
#String operator using seperator case
"""s="Hello_world_of_python"
print(s[::])
print(s[:])
print(s[0:9:1])
print(s[0:9:2])
print(s[2:4:1])
print(s[::2])
print(s[2::])
print(s[:4:])
print(s[-4::-1])
print(s[-8::])
print(s[-1::-2])
print(s[-3:3:-1])
print(s[-15:-3:1])
#et cetra
"""

#6.5 |__________________________
#STRING IN PYTHON IS IMMUTABLE
"""name="lord puneet"
print(name)
print(name[0])
name[0]='n'"""

#6.6 |___________________________
#Operators On Strings(+,*[only])
"""a="python"
b="programing"
c=4
print(a+b)
print(a*c)
#print(a+c)error
#print(a*b)
print(type(a*c))"""

#6.7 |___________________
#Length Of String(len())
"""a="Hello_World"
print(a)
print("Length of String is= ",len(a))"""

#6.8 |__________________________________________________
#Membership Operator in Python For STRINGS (in, not in)
"""a="Hello_World"
print("o" in a)
print("a" in a)
print("a" not in a)
print("orld" not in a)
print("orld" in a)"""

#6.9 |________________________________________
#To Find Substring in Main String (in, not in)
"""main=input("Enter Main String: ")
sub=input("Enter Sub String: ")
if sub in main:
    print(sub,"is found in main string")
else:
    print(sub,"is not found in main string")
if sub not in main:
    print(sub,"is not found in main string")
else:
    print(sub,"is found in main string")"""

#6.10 |__________________________________________
#Comparison Operators On Strings(<=,>=,<,>,==,!=)

#eg one | basics
"""s1="abcd"
s2="abcdefg"
print(s1==s2)
print(s1<=s2)
print(s1>=s2)
print(s1<s2)
print(s1>s2)
print(s1!=s2)"""

#eg two | Check user name
"""name="Shlok"
user_name=input("Enter User Name: ")
if user_name==name:
    print("Welcom!")
else:
    print("Invalid User Name, try again")"""
