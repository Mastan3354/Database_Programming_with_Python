
##1). Program to Connect with Postgresql Database and print it's Version.
# import psycopg2

# #establishing the connection
# conn = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
# print("Postgresql database version : ",conn.server_version)

# #Closing the connection
# conn.close()



##2). Write a Program to Create Employees Table in the Postgres Database employees (eno,ename,esal,eaddr).
# import psycopg2
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     cursor.execute("create table employees(eno int,ename char(10),esal decimal(10,2),eaddr char(10))") 
#     con.commit()
#     print("Table created successfully") 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##3). Write a Program to Drop Employees Table from Postgresql Database
# import psycopg2
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432') 
#     cursor=con.cursor() 
#     cursor.execute("drop table employees")
#     con.commit()
#     print("Table dropped successfully") 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##4). Write a Program to Insert a Single Row in the database table.
# import psycopg2
# try:
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')  
#     cursor=con.cursor() 
#     cursor.execute("insert into employees values(3354,'Mastan',1000,'Hyd')") 
#     con.commit() 
#     print("Record Inserted Successfully") 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##5). Write a Program to Insert Multiple Rows in the Employees Table by using executemany() Method
# import psycopg2
# try:
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432') 
#     cursor=con.cursor() 
#     sql="insert into employees values(%s, %s, %s, %s)" 
#     records=[(3356,'A',1200,'Mumbai'), 
#     (3357,'B',1300,'Hyd'), 
#     (3358,'C',1400,'Hyd')] 
#     cursor.executemany(sql,records) 
#     con.commit() 
#     print("Records Inserted Successfully") 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##6). Write a Program to Insert Multiple Rows in the Employees Table with Dynamic Input from the Keyboard.
# import psycopg2 
# try:

#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     while True:
#         eno=int(input("Enter Employee Number:")) 
#         ename=input("Enter Employee Name:") 
#         esal=float(input("Enter Employee Salary:")) 
#         eaddr=input("Enter Employee Address:") 
#         sql="insert into employees values(%d,'%s',%f,'%s')" 
#         cursor.execute(sql %(eno,ename,esal,eaddr)) 
#         print("Record Inserted Successfully") 
#         option=input("Do you want to insert one more record[Yes|No] :") 
#         if option=="No": 
#             con.commit() 
#             break
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##7). Write a Program to Update Employee Salaries with Increment for the certain Range with Dynamic Input ​
##Eg: Increment all employee salaries by 500 whose salary < 5000
# import psycopg2
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     increment=float(input("Enter Increment Salary:")) 
#     salrange=float(input("Enter Salary Range:")) 
#     sql="update employees set esal=esal+%f where esal<%f" 
#     cursor.execute(sql %(increment,salrange)) 
#     print("Records Updated Successfully") 
#     con.commit() 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##8). Write a Program to Delete Employees whose Salary Greater provided Salary as Dynamic Input?​
##Eg: delete all employees whose salary > 5000
# import psycopg2 
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     cutoffsalary=float(input("Enter CutOff Salary:"))
#     sql="delete from employees where esal>%f" 
#     cursor.execute(sql %(cutoffsalary)) 
#     print("Records Deleted Successfully")
#     con.commit() 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##9). Write a Program to Select all Employees info by using fetchone() Method.
# import psycopg2 
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     cursor.execute("select * from employees") 
#     row=cursor.fetchone() 
#     while row is not None: 
#         print(row) 
#         row=cursor.fetchone() 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback()
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##10). Write a Program to select all Employees info by using fetchall() Method.
# import psycopg2
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor()
#     cursor.execute("select * from employees") 
#     data=cursor.fetchall() 
#     for row in data: 
#         print("Employee Number:",row[0]) 
#         print("Employee Name:",row[1]) 
#         print("Employee Salary:",row[2]) 
#         print("Employee Address:",row[3]) 
#         print() 

# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback() 
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()



##11). Write a Program to select Employees info by using fetchmany() Method and the required Number of Rows will be provided as Dynamic Input.
# import psycopg2 
# try: 
#     con = psycopg2.connect(database="trainee-sessions", user='postgres', password='password', host='127.0.0.1', port= '5432')
#     cursor=con.cursor() 
#     cursor.execute("select * from employees") 
#     n=int(input("Enter the number of required rows:")) 
#     data=cursor.fetchmany(n) 
#     for row in data: 
#         print(row) 
# except psycopg2.DatabaseError as e: 
#     if con: 
#         con.rollback()
#         print("There is a problem with sql :",e) 
# finally: 
#     if cursor: 
#         cursor.close() 
#     if con: 
#         con.close()