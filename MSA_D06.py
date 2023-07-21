#5.2.1 |__________________________
#To print pattern using for loop

#Pattern one 
"""for i in range(1,6):
    for j in range (1,6):
        print(j,end=' ')
    print()"""

#Pattern two
"""for i in range(1,6):
    for j in range (1,i+1):
        print(j,end=' ')
    print()"""

#Pattern three
"""for i in range(1,6):
    for j in range (1,i+1):
        print(i,end=' ')
    print()"""

#Pattern four
"""for i in range(1,7):
    for j in range (1,i+1):
        add=i+j
        if(add%2==0):
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()"""

#Pattern five
"""for i in range(1,6):
    for j in range (1,i+1):
        print("*",end=' ')
    print()"""

#Pattern six
"""for i in range(5,0,-1):
    for j in range (i,0,-1):
        print("*",end=' ')
    print()"""

#Pattern seven (imp)
"""for i in range(1,6):
    for j in range (1,6-i):
        print(" ",end=' ')
    for k in range (1,i+1):
        print("*",end=' ')
    print()"""

#Pattern eight (imp)
"""for i in range(1,6):
    for j in range (1,6-i):
        print(" ",end=' ')
    for k in range (1,i+1):
        print("*  ",end=' ')
    print()"""

#Pattern nine (imp)
"""for i in range(1,6):
    for j in range (1,6-i):
        print(" ",end=' ')
    for k in range (0,2*i-1):
        print("*",end=' ')
    print()"""

#Pattern 10(imp)
"""for i in range(6):
    for j in range (6-i):
        print(" ",end=' ')
    p=i
    for k in range (i):
        print(p,end=' ')
        p+=1
    p=p-2
    for l in range (1,i):
        print(p,end=' ')
        p-=1
    print()"""
