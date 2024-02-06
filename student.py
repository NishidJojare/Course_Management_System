import mysql.connector
try:
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")
    
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM tblcourse")
    
    data=mycursor.fetchall()
    
    for row in data:
        print(row)
        
except Exception as e:
    print(e)
    mycursor.execute('SELECT * FROM tblcourse')
    data=mycursor.fetchall()
    for row in data:
        print(row)   
except:
    pass 