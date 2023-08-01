#____________________________________________________________________________________
#DAY 21

#_________________
#Operator Overloading

#Working of Magic Operator

# eg two | ()

            # will give error
"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student("Samvida",100)
s2=student("Surya",200)
print("s1>s2 =",s1>s2)
print("s1<s2 =",s1<s2)
print("s1<=s2 =",s1<=s2)
print("s1>=s2 =",s1>=s2)"""

            # correct way by using magic operator
"""class student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self,other):
        return self.marks>other.marks

    def __lt__(self,other):
        return self.marks<other.marks

    def __ge__(self,other):
        return self.marks >=other.marks

    def __le__(self,other):
        return self.marks <=other.marks
    
s1=student("Samvida",100)
s2=student("Surya",200)
print("s1>s2 =",s1>s2)
print("s1<s2 =",s1<s2)
print("s1<=s2 =",s1<=s2)
print("s1>=s2 =",s1>=s2)"""


#_________________
#Method Overloading

#using if elif else
"""class Demo:

    def sum (self, a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum of",a,",",b,"&",c,"is =",a+b+c)
        elif a!=None and b!=None:
            print("Sum of",a,"&",b,"is =",a+b)
        elif a!=None:
            print("Sum  of",98a,"&",a,"is =",a+a)
        else:
            print("No number is passed as argument")

d=Demo()
d.sum(5,6,7)
d.sum(5,6)
d.sum(5)
d.sum()"""

# By variable Length

"""class Demo:

    def sum(self,*a):
        total=0
        print(type(a))
        for x in a:
            total=total+x
        print("The Sum:",total)

d=Demo()
d.sum(5,6,7)
d.sum(5,6)
d.sum(5)
d.sum()"""

#W.A.P To Make function which tell different things according to ARGUMENTS

"""class Demo:
    def calc(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            if a>b and a>c:
                print (a,"is the greatest")
            elif b>c:
                print (b,"is the greatest")
            else:
                print (c,"is the greatest")
            
        elif a!=None and b!=None:
            print("Sum of",a,"&",b,"is =",a+b)
            print("Sub of",a,"&",b,"is =",a-b)
            
        elif a!=None:
            fac=1
            for i in range (1,a+1):
                fac=fac*i
            print("Factorial of",a,"is =",fac)
            
        else:
            print("No number is passed as argument")

d=Demo()
d.calc(5,6,7)
d.calc(5,6)
d.calc(5)
d.calc()"""

#_______________________
# Constructor Overloading

#
"""class Demo:

    def __init__(self,a=None,b=None,c=None):

         print(a)
         print(b)
         print(c)

d1=Demo(10,20)"""

# By variable Length
"""class Demo:

    def __init__(self,*a):
        total=0
        for x in a:
            total+=x
        print("sum =",total)
         
d1=Demo()
d2=Demo(10)
d3=Demo(10,20)
d4=Demo(10,20,30)
d5=Demo(10,20,30,40)"""

#
#Overriding in Python

#Method overriding
"""class P:
    def properties_status(self):
        print("Money,Land,Gold")
    def to_marry(self):
        print("Anushka")

class C(P):
    def study_status(self):
        print("Studies done waiting for job")
    def to_marry(self):
        print("megha")

c=C()
c.properties_status()
c.to_marry()
c.study_status()"""
