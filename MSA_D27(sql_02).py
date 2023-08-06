#_____________________________________________________________________________________________________________________________________
#DAY 27

#_______________________________________________________________________________________________
#------------------+
# WORKING OR MYSQL |
#------------------+

#___________________________________
# To insert Data In Table
"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()
sql = "INSERT INTO students (name,course) VALUES (%s, %s)"
val = (
    ('Priyanshu','ECE'),
    ('Pallavi','MCA'),
    ('turn','MPA'),
    ('sushant', 'MPA'),
    ('jitin', 'BCOM'),
    ('nitin', 'BCOM'),
    ('raman', 'CSA'),
)

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")"""

#_____________________________
# To display all data of Table
"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)"""

#___________________________________
# To display only one data of Table

"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT name , course FROM students")

myresult=mycursor.fetchone()

for x in myresult:
    print(x)"""

#________________________________________
# To display specific data using where
"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students WHERE course = 'BCOM'")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)"""

#________________________________________
# To display specific data using where
"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students WHERE name LIKE '%ram%'")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)"""

#______________________________________________________
# To display ordered data (by default increasing order)

"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students ORDER BY name")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)"""

#____________________________________________
# To display ordered data in Decresing Order

"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students ORDER BY name DESC")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)"""


#_______________________________________
# To Delete Data in Table Using DELETE
"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("DELETE FROM students WHERE course = 'BCOM'")

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")"""

#___________________________________________________________________
# To Delete Data in Table Using DELETE and display all left data
"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

mycursor.execute("DELETE FROM students WHERE course = 'BCOM'")

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")

mycursor.execute("SELECT * FROM students")

myresult=mycursor.fetchall()

for x in myresult:
    print(x)"""

#_______________________________________________________
# To Update Data in Table Using UPDATE and Display them

"""import mysql.connector as sql

mydb= sql.connect(
    host="localhost",
    user="root",
    password="",
    database="vsics_database01"
)
mycursor = mydb.cursor()

sql = "UPDATE students SET course = 'CSE' WHERE course = 'ECE' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount,"record(s) affected")

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)"""
