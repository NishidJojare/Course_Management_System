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