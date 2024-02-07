import mysql.connector
from datetime import timedelta
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
            

        
    def Search_Student(self):
          
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")
            mycursor=mydb.cursor()
            
            search_input=input('Enter Student Id or Name : ')
            
            if search_input.isdigit():
                
                mycursor.execute("SELECT * FROM tblcourse WHERE Stud_Id=%s",(search_input,))
                row=mycursor.fetchone()
                
                if row:
                    print('---------------------------------------------')
                    print(f'Id : {row[0]}\nName : {row[1]}\nMobile : {row[2]}\nAddress : {row[3]}\nCourse : {row[4]}\nJoining Date : {row[5]}\nExpected Date of Completion : {row[5]+timedelta(days=75)}\n')
                    print('---------------------------------------------\n')
                else:
                    print('Student not found...')
            
            else:
                mycursor.execute("SELECT * FROM tblcourse WHERE Name=%s",(search_input,))
                self.record=mycursor.fetchall()
                
                if self.record:
                    for row in self.record:
                          print('---------------------------------------------')
                          print(f'Id : {row[0]}\nName : {row[1]}\nMobile : {row[2]}\nAddress : {row[3]}\nCourse : {row[4]}\nJoining Date : {row[5]}\nExpected Date of Completion : {row[5]+timedelta(days=75)}\n')
                         
                else:
                    print('Student not found...')
                
            mydb.commit()
            mycursor.close()
            mydb.close()
        
                
        except Exception as e:
                print(e) 
            
    
    
        