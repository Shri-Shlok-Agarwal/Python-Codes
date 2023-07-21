#___________________________________________________________________________________________
#DAY 11

#__________________________________________________________________________
#1 | TYPES OF FUNCTION ARGUMENT

#____________________________________
#1.1 | WAP to Pass KEYWORD ARGUMENTS
"""def cart(item,price):
    print(item,"cost is :",price)
cart(item="electronics",price=20000)
cart(item="motorbike",price=100000)
cart(price=1100,item="shirt")
cart("jeans",1200)"""

#______________________________________________
#1.2 | WAP Calling Function With KEY ARGUMENTS
"""def details(id,name):
    print("emp id is :",id)
    print("emp name is : ",name)
#calling function
details(2871,name="Shlok")"""

#________________________________
#1.3 | Positional Argument error
"""def details(id,name):
    print("emp id is :",id)
    print("emp name is : ",name)
#calling function
details(name="elvish yadav",id=1) #if id= is written then positional error is corected
details(name="elvish yadav",1) #positional argument error"""

#___________________________________________
#1.4 | DEFAULT Function Argument Definition
"""def cart(item,price=20):
    print(item,"cost is :",price)
cart(item="pen")
cart(item="handbag",price=10000)
cart(price=500,item="shirt")"""

#________________________________
#1.5 | VARIALBE LENGTH Arguments
"""def total_cost(x,*y):
    sum=0
    for i in y:
        sum+=i
    print(x+sum)
#calling function
total_cost(100,200)
total_cost(110,226,311)
total_cost(11,)
total_cost(99.9,89.8)"""
        #or
"""def total_cost(*y):
    sum=0
    for i in y:
        sum+=i
    print(sum)
#calling function
total_cost(100,200)
total_cost(110,226,311)
total_cost(11,)
total_cost(99.9,89.8)"""
        #or
"""a=[10,20,30,40]
def total_cost(*y):
    sum=0
    for i in y:
        sum+=i
    print(sum)
total_cost(a)"""


#___________________________________________________
#1.6 | Keyword Variable LENGHT Argument (**Variable)
"""def m1(**x):
    for k,v in x.items():
        print(k,"=",v)
m1(a=10,b=50,c=100)
m1(id=1,name="shubhalaxmi")"""
