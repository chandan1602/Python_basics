#step 1
import sqlite3

#step 2
#connection_var=sqlite3.connect("database/database.sqlite/database.db")

con=sqlite3.connect("chandan")
if con:
    print("database craeted")
else:
    print("error")

'''
DML
----------
    insert, delete, update
    |
    commit()

sql queries
-------------------
    execute() method is used.

    syntax
    -----------
    connect_var.execute("query")
    connect_var.commit()

'''
#con.execute("create table stu(id int,name text)");

'''
con.execute("insert into stu values(1,'abc')")
con.commit()
print("Data inserted")
'''

id=int(input("Enetr Id: "))
name=input("Enter Name:")
'''
format specifier
------------------
    %d   int
    %s   string
    %f   float

    connection_var.execute("insert into tablename values(format_specifier)"%(var1,var_n))
'''
con.execute("insert into stu values(%d,'%s')"%(id,name))
con.commit()
print("Data inserted")


'''
cursor_object=connection_var.cursor()
cursor_object.execute("sql query")

'''
cur=con.cursor()
'''
cur.execute("select * from stu")
print(cur.fetchone())

cur.execute("select * from stu")
print(cur.fetchall())
'''
cur.execute("select * from stu")
'''
for x in cur:
    print(x)
'''
print("id          name")
print("------------------")
for x in cur:
    print(x[0],"  ",x[1])





