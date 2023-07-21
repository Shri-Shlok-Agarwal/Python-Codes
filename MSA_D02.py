#_________________________________________________________________________________________________________
#DATA TYPES

#__________________________________________________
#To Print int Data, to modify it and print its type 
"""a=5
print(a)
a=7
print(a)
print(type(a))"""

#_________________
#float new concept
"""a=2e2
b=2E2
c=2e3
print(a)
print(b)
print(c)
print(type(a)"""

#__________________
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

#__________________
#boolean data type
"""a=True
b=False
print(a)
print(b)
print(a+a)
print(a+b)"""

#_______________
#none data type
"""a=None
print(a)
print(type(a))"""

#_________________
#string data type
"""name1="Shlok"
name2='Agarwal'
print(name1,name2)"""

#_______________
#Bytes data type
"""a=[10,20,30]
b=bytes(a)
#b[1]=40 error immutable
print(a[1])
print(b[1])"""

#______________________________________________________________________
#BYTE ARRAY Function
"""a=[10,20,30]
b=bytearray(a)
b[1]=40 #will run mutable
print(a[1])
print(b[1])"""

#_______________________________________________________________________
#Creating List Using Range
"""l=list(range(1,20))
print(l)"""

#_______________________________________________________________________________________________________________________
#OPERATORS
#__________________________________
#Arithmetic Operator(+,-,*,/,**,//)

#________________________________________
#RelationshipOperator(>,<,==,>=,<=,!=)
"""a=5
b=9
print(a!=b)"""

#____________________
#Logical Operatorx=6
"""x=6
y=5
z=8
print(z and x and y)
print(z or x or y)
print(z and x or y)
print(z or x and y)
print(x not and y)"""

#______________________
#Unary Operator(-a,+a)
"""a=8
print(a)
print(-a)"""

#______________________________
#Membership Operator(in,not in)
"""L=["shlok","vishal","rana"]
print("shlok" in L)
print("Ankit" in L)
print("vishal" in L)
print("rana" not in L)"""

#_____________________________
#Identity Operator(is,is not)
"""a=25
b=25
print(a is b)
print(a is not b)
print(id(a))
print(id(b))"""
