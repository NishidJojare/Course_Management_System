from student import Student
from datetime import date
from course import Course
objstudent=Student()
objCourse=Course()

def Menu():
    try:
        while True:
            print("Choose any Menu:\n\n\t1. Show all Students \n\t2. Add Student\n\t3. View Batch-Wise Stats\n\t4. Search Student\n\t5. Exit\n")
            menu=int(input("Enter a menu: "))
            objCourse.define_courses()
            if menu==1:
                objCourse.get_python_batch()
                print()
                objCourse.get_da_batch()
                print()
                objCourse.get_ds_batch()
                
            elif menu==2:
                name=input("Enter name of student: ")
                mobile=int(input("Enter mobile number of student: "))
                address=input("Enter address of student: ")
                course_name=input("Enter a course name: ")
                joining_date=date.today()
                
                objstudent.Addstudent(name,mobile,address,course_name,joining_date) 
                
            elif menu==3:
                
               objCourse.show_batch_wise_stats()
        
            elif menu==4:
                objstudent.Search_Student()
              
            elif menu==5:
                break  
            
            else:
                print('Please enter valid menu...\n')
    
    except Exception as e:
        print(e)
        
Menu()
        
          