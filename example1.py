
##1). Program to connect with sqlite database
# import sqlite3
# conn = sqlite3.connect('test.db')
# print("Opened database successfully")



##2). Write a Program to Create Table, Insert Data and display Data by using Sqlite Database.
# import sqlite3
# try: 
#     con=sqlite3.connect("test.db")
#     cursor=con.cursor() 
#     cursor.execute("create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
#     print("Table Created...") 

#     sql = "insert into employees values(?, ?, ?, ?)" 
#     records=[(1,'Sharad',2000,'Hyd'), (2,'Kishore',2500,'Hyd'), (3,'Sai Ram',3000,'')] 
#     cursor.executemany(sql,records)
#     con.commit() 
#     print("Records Inserted Successfully...") 

#     cursor.execute("select * from employees") 
#     data=cursor.fetchall() 
#     for row in data: 
#         print("Employee Number:",row[0]) 
#         print("Employee Name:",row[1]) 
#         print("Employee Salary:",row[2]) 
#         print("Employee Address:",row[3]) 
#         print() 
# except sqlite3.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##3). Write a Program to Copy Data present in Employees Table of Sqlite Database into Postgres Database.
# import sqlite3 
# import psycopg2 
# try: 
#     con=sqlite3.connect("test.db")
#     cursor=con.cursor() 
#     cursor.execute("select * from employees") 
#     data=cursor.fetchall() 
#     list=[] 
#     for row in data: 
#         t=(row[0],row[1],row[2],row[3]) 
#         list.append(t)
#     print("Fetched Records from MySQL Database")
# except sqlite3.DatabaseError as e:
#     if con: 
#         con.rollback() 
#         print("There is a problem with MySql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close() 

# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     sql="insert into employees values(%s,%s,%s,%s)" 
#     cursor.executemany(sql,list) 
#     con.commit() 
#     print("Records Copied from MySQL Database to Oracle Database Successfully") 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()