import mysql.connector
try:
    def connection(query, parameter=None):
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="main"
            ) 
        
        my_cursor=con.cursor()
        my_cursor.execute(query, parameter)
        result=my_cursor.fetchall()
        con.commit()
        con.close()
        return result
        
except:
    pass