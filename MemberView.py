from mysql import connector
from datetime import datetime

class GymManager:
    def __init__(self):
        self.connection =connector.connect(
            user     = "root",
            password ="Navneetha@2005",
            database ="gym_db_aug26",
            host     ="localhost"
        ) 
        print("Connect Sucessfully.....")
    def get_object(self,id =None):
        try:
            self.cursor =self.connection.cursor()
            query ="select * from member where id=%s"
            values =(id,)
            self.cursor.excute(query,values)
            record =self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
            
    def post(self,**kwargs):
        try:
            self.cursor =self.connection.cursor()
            query ="""insert into member(name,place,mobile,plan,fee,joining_date)  
            values(%s,%s,%s,%s,%s,%s)"""   
            values =[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Data inserted sucessfully....!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from Member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for i  in records:
                print(i)
        except Exception as e:
            print(e)
    def retrieve(self ,id=None):
        try:
            record =self.get_object(id=id)
            if record==None:
             print("No gym member found....!")
            print(record)    
        except Exception as e:
            print(e)           
             
member_instance =GymManager() 
#member_instance.post (name="Asliya",place="kakkand",mobile ="9867554313",plan="2 month",fee =15000,joining_date =datetime.today())  
member_instance.get()
# member_instance.retrieve(id=2)
              
               
    
    
