#___________________________________________________________________________________________________________________________
#DAY 16

#_____________________________________________________________________________
#DICTIONARIES IN PYTHON

#_________________
#Creating Dictionaries

# eg one |
"""d={1:"Aniket",2:"singh",3:"Shlok",4:"Agarwal"}
print(d)"""

# eg two |
"""d={}
d[1]="VSICS"
d[2]="Saket"
d[3]="Nagar"
print(d)"""

#_____________________________________
#Accessing Dictonaries

#By Using Keys
"""d={1:"Aniket",2:"singh",3:"Shlok",4:"Agarwal"}
print(d[1])
print(d[2])
print(d[3])
print(d[4])
print(d[5])"""      #key not availabe hence shows KeyError

#W.A.P to get and show Employee Information
"""d={}
n=int(input("Enter number of Employees"))
i=1
while(i<=n):
    name=input("Enter Employee Name")
    salary=int(input("Enter Employee Salary"))
    d[name]=salary
    i+=1
for x in d:
    print("The Name is: ",x,"and his salary is: ",d[x])"""

#_______________________________________
#Updating A DICTONARY

# case one |
"""d={1:"Aniket",2:"singh",3:"Shlok",4:"Agarwal"}
print("Old Dictionary: ",d)
d[10]="Shree Hari"
print("Added key-value(10:Shree Hari) pair to dictionary: ",d)"""

# case two |

#_________________________________________
#Delete Method to delete item in dictionary

#Delete Method to delete item in dictionary
"""d={1:"Aniket",2:"singh",3:"Shlok",4:"Agarwal"}
print("Before Deleting: ",d)
del d[1]
del d[2]
print("After Deleting: ",d)"""

#By Using Clear Method to remove all the Elements
"""d={1:"Aniket",2:"singh",3:"Shlok",4:"Agarwal"}
print("Before Clearing Entries: ",d)
d.clear()
print("After Clearing Entries: ",d)"""
