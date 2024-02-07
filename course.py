
from datetime import date,datetime,timedelta
import mysql.connector
class Course:
    def __init__(self):
        self.pyDuration=75
        self.daDuration=75 
        self.dsDuration=75
        
        self.table={"Python-Django":{'Batch A':[],'Batch B':[]},
                    "Data Analytics":{'Batch A':[],'Batch B':[]},
                    "Data Science":{'Batch A':[],'Batch B':[]}
                    }
      


    def define_courses(self):
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM tblcourse")
            data=mycursor.fetchall()
            
            for row in data:
                if row[4].lower()=='python-django':
                    if len(self.table['Python-Django']['Batch A'])<5:
                    
                        data={'Name':row[1],'Date of Joining':row[5]}
                        self.table["Python-Django"]["Batch A"].append(data)
                        
                    else:
                        data={'Name':row[1],'Date of Joining':row[5]}
                        self.table["Python-Django"]["Batch B"].append(data)
                        
                        
                if row[4].lower()=='data analytics':
                    if len(self.table['Data Analytics']['Batch A'])<5:
                        
                        data={'Name':row[1],'Date of Joining':row[5]}
                        self.table["Data Analytics"]["Batch A"].append(data)
                        
                    else:
                        data={'Name':row[1],'Date of Joining':row[5]}
                        self.table["Data Analytics"]["Batch B"].append(data)
                        
                    
                if row[4].lower()=='data science':
                    if len(self.table['Data Science']['Batch A'])<5:
                        
                        data={'Name':row[1],'Date of Joining':row[5]}
                        self.table["Data Science"]["Batch A"].append(data)
                        
                    else:
                        data={'Name':row[1],'Date of Joining':row[5]}
                        self.table["Data Science"]["Batch B"].append(data)
                    
                    
            return self.table
        
    def py_course_duration(self, batch):
        # self.course_start_date='01-11-2023' 
        
       
        # calculating course duration for python-django batch(both A and B)
        if len(self.table['Python-Django'][batch]) != 0:
            print('**************** Python-Django ****************')
            
           
            for row in self.table['Python-Django'][batch]:
                name = row['Name']
                date_of_joining = row['Date of Joining']
                expected_completion_date = date_of_joining + timedelta(days=self.pyDuration)
                
                print(f"Name: {name}\nDate of Joining: {date_of_joining.strftime('%d-%m-%Y')}")
                print(f"Expected Completion Date: {expected_completion_date.strftime('%d-%m-%Y')}\n")
    
    
    # calculating course duration for Data Analytics batch(both A and B)
    def da_course_duration(self,batch):
        self.course_start_date='01-11-2023' 
        
            
        if len(self.table['Data Analytics'][batch]) != 0:
            print('**************** Data Analytics ****************')  
              
    
            for row in self.table['Data Analytics'][batch]:
                name = row['Name']
                date_of_joining = row['Date of Joining']
                expected_completion_date = date_of_joining + timedelta(days=self.daDuration)
                
                print(f"Name: {name}\nDate of Joining: {date_of_joining.strftime('%d-%m-%Y')}")
                print(f"Expected Completion Date: {expected_completion_date.strftime('%d-%m-%Y')}\n")
    
    
    # calculating course duration for Data Science batch(both A and B)
    def ds_course_duration(self,batch):
        self.course_start_date='01-01-2024' 
          
        
        if len(self.table['Data Science'][batch]) != 0:
            print('**************** Data Science ****************') 
          
            for row in self.table['Data Science'][batch]:
                name = row['Name']
                date_of_joining = row['Date of Joining']
                
                expected_completion_date = date_of_joining + timedelta(days=self.dsDuration)
                
                
                print(f"Name: {name}\nDate of Joining: {date_of_joining.strftime('%d-%m-%Y')}")
                print(f"Expected Completion Date: {expected_completion_date.strftime('%d-%m-%Y')}\n")   
    
    
    def get_python_batch(self):
        
        self.py_course_duration("Batch A")
        self.py_course_duration("Batch B")
    
    
    def get_da_batch(self):
    
        self.da_course_duration("Batch A")
        self.da_course_duration("Batch B")
            
            
            
    def get_ds_batch(self):
        
        self.ds_course_duration("Batch A")
        self.ds_course_duration("Batch B")
        
        
      
    def calculate_delays(self,end_date):
        
        current_date=date.today()
        delay_days=end_date-current_date
        return delay_days.days
        
    
        
    def show_batch_wise_stats(self):
        
        batch_a_start_date_python = date(2024,1,1)  
        batch_b_start_date_python = date(2023,11,10)  
            
        batch_a_completion_date_python=batch_a_start_date_python + timedelta(days=self.pyDuration) 
        batch_b_completion_date_python=batch_b_start_date_python + timedelta(days=self.pyDuration) 
            
        delaysA_python=self.calculate_delays(batch_a_completion_date_python)
        delaysB_python=self.calculate_delays(batch_b_completion_date_python)
        
        #################
        batch_a_start_date_da = date(2024,1,1)  
        batch_b_start_date_da = date(2023,10,15)  
            
        batch_a_completion_date_da=batch_a_start_date_da + timedelta(days=self.daDuration) 
        batch_b_completion_date_da=batch_b_start_date_da + timedelta(days=self.daDuration) 
            
        delaysA_da=self.calculate_delays(batch_a_completion_date_da)
        delaysB_da=self.calculate_delays(batch_b_completion_date_da)
        
        #############
        
        batch_a_start_date_ds = date(2024,1,1)  
        batch_b_start_date_ds = date(2023,10,10)  
            
        batch_a_completion_date_ds=batch_a_start_date_ds + timedelta(days=self.dsDuration) 
        batch_b_completion_date_ds=batch_b_start_date_ds + timedelta(days=self.dsDuration) 
            
        delaysA_ds=self.calculate_delays(batch_a_completion_date_ds)
        delaysB_ds=self.calculate_delays(batch_b_completion_date_ds)
       
        print(f'''
              1. Python
                           a. Batch A - Start: {batch_a_start_date_python} : | End : {batch_a_completion_date_python} | Status : {"Ongoing" if delaysA_python>0 else f"Delayed by {abs(delaysA_python)} days"}
                           b. Batch B - Start: {batch_b_start_date_python} : | End : {batch_b_completion_date_python} | Status : {"Ongoing" if delaysB_python>0 else f"Delayed by {abs(delaysB_python)} days"}

               2. Data Analytics 
                            a. Batch A - Start: {batch_a_start_date_da} : | End : {batch_a_completion_date_da} | Status : {"Ongoing" if delaysA_da>0 else f"Delayed by {abs(delaysA_da)} days"}
                            b. Batch B - Start: {batch_b_start_date_da} : | End : {batch_b_completion_date_da} | Status : {"Ongoing" if delaysB_da>0 else f"Delayed by {abs(delaysB_da)} days"}

               3. Data Science   
                            a. Batch A - Start: {batch_a_start_date_ds} : | End : {batch_a_completion_date_ds} | Status : {"Ongoing" if delaysA_ds>0 else f"Delayed by {abs(delaysA_ds)} days"}
                            b. Batch B - Start: {batch_b_start_date_ds} : | End : {batch_b_completion_date_ds} | Status : {"Ongoing" if delaysB_ds>0 else f"Delayed by {abs(delaysB_ds)} days"}
              ''')   
        