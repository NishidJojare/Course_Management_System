import mysql.connector
class Student:  
    def Addstudent(self,name,mobile,address,course_name,joining_date,date_of_completion=None,batch=None):
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")
        try:
            mycursor=mydb.cursor()
            mycursor.execute("INSERT INTO tblcourse(Name,Mobile,Address,Course_Name,Joining_Date,Date_Of_Completion,Batch) VALUES (%s,%s,%s,%s,%s,%s,%s)", (name,mobile,address,course_name,joining_date,date_of_completion,batch))
            mydb.commit()
            mycursor.close()
            mydb.close()
            
           
        except Exception:
            print(f"Something went wrong")  
            
            
            
    def show_all_students(self):  
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM tblcourse")
            data=mycursor.fetchall()
           
            for row in data:
                print(row)
                
            mydb.commit()
            mycursor.close()
            mydb.close()
    
            
        except Exception as e:
            print(e) 
            

        
               
               
            
    
            
    
    