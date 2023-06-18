import mysql.connector  
import csv
import datetime
cs=open("txtsql_files\\festival_file.txt",'r')
reader=csv.reader(cs)
con=mysql.connector.connect(host="localhost",user="root",passwd="",database="main")
my_cursor=con.cursor()
for i in reader:
    print(i)
    #my_cursor.execute("INSERT INTO fest_india(id, fest_name, fest_date,locality) VALUES (%s, %s, %s,%s)",i)    
con.commit()
dt=datetime.datetime.now()
print(dt.date())
print(my_cursor._rowcount, "record inserted.")
