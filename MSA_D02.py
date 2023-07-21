#_______________________________________________________________________________________________________________________________________________________________________
#DAY 01
#1 |________________________________________________________________________________________________________
#DATA TYPES

#1.1 |________________________________________________
#To Print int Data, to modify it and print its type 
"""a=5
print(a)
a=7
print(a)
print(type(a))"""

#1.2 |_____________
#float new concept
"""a=2e2
b=2E2
c=2e3
print(a)
print(b)
print(c)
print(type(a)"""

#1.3 |______________
#complex data type
"""a=3+5j
b=2-5.5j
c=3+10.5j
print(a)
print(b)
print(c)
print(a+b )
print(a+c)
print(a>b)#error"""

#1.4 |______________
#boolean data type
"""a=True
b=False
print(a)
print(b)
print(a+a)
print(a+b)"""

#1.6 |___________
#none data type
"""a=None
print(a)
print(type(a))"""

#1.7 |_____________
#string data type
"""name1="Shlok"
name2='Agarwal'
print(name1,name2)"""

#1.8 |___________
#Bytes data type
"""a=[10,20,30]
b=bytes(a)
#b[1]=40 error immutable
print(a[1])
print(b[1])"""

#IMP |___________________________________________________________________
#BYTE ARRAY Function
"""a=[10,20,30]
b=bytearray(a)
b[1]=40 #will run mutable
print(a[1])
print(b[1])"""

#IMP |______________________________________________________________________
#Creating List Using Range
"""l=list(range(1,20))
print(l)"""

#2 |_____________________________________________________________________________________________________________________
#OPERATORS
#2.1 |______________________________
#Arithmetic Operator(+,-,*,/,**,//)

#2.2 |____________________________________
#RelationshipOperator(>,<,==,>=,<=,!=)
"""a=5
b=9
print(a!=b)"""

#2.3 |________________
#Logical Operatorx=6
"""x=6
y=5
z=8
print(z and x and y)
print(z or x or y)
print(z and x or y)
print(z or x and y)
print(x not and y)"""

#2.4 |__________________
#Unary Operator(-a,+a)
"""a=8
print(a)
print(-a)"""

#2.5 |__________________________
#Membership Operator(in,not in)
"""L=["shlok","vishal","rana"]
print("shlok" in L)
print("Ankit" in L)
print("vishal" in L)
print("rana" not in L)"""

#2.6 |_________________________
#Identity Operator(is,is not)
"""a=25
b=25
print(a is b)
print(a is not b)
print(id(a))
print(id(b))"""
