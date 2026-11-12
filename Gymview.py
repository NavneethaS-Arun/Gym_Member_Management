from mysql import connector
from datetime import datetime


class DbConnect:
    def get_connection(self):
        try:
            self.connection =connector.connect(
                user = "root",
                password ="Navneetha@2005",
                database ="gym_db_aug26",
                host = "localhost" ,
            )
            return self.connection
        except Exception as e:
            return None
        
    
class GymMemberManagement(DbConnect): 
    
    def get_object(self,id=None):
            try:
                self.cursor = self.connection.cursor()
                query="select * from member where id=%s"
                Values=(id,)
                self.cursor.execute(query,Values)
                record=self.cursor.fetchone()
                return record
            except Exception as e:
                print(e)
                       
    def get(self):
        try: 
                self.connection=super().get_connection()
                self.cursor=self.connection.cursor()
                query="select * from member"
                self.cursor.execute(query)
                records=self.cursor.fetchall()
                if records:
                    for i in records:
                        print(i)
                else:
                    print("No Records")
        except Exception as e:
            print(e)
            
            
    def post(self, **kwargs):
            try:
                self.connection=super().get_connection()
                self.cursor = self.connection.cursor()
                query = """insert into member(name,place,mobile,plan,fee,joining_date)
                values(%s, %s, %s, %s, %s, %s)"""
                values=[v for v in kwargs.values()]
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Data inserted Successfully")
            except Exception as e:
                print(e)
                
    def retrieve(self,id=None):
            try:
                
                record=self.get_object(id=id)
                if record == None:
                    print("No Members Found..!")
                else:
                    print(record)
            except Exception as e:
                print(e)
    def delete(self, id = None):
        try:
            record = self.get_object(id = id)
            if record != None:
                query = "delete from member where id = %s"
                self.cursor.execute(query, (id,))
                self.connection.commit()
                print("Data Deleted Successfully..")
            else:
                print("No data found..")
        except Exception as e:
            print(e)            
    def put(self ,id =None,**kwargs):
        try:
            record =self.get_object(id=id)
            if record !=  None:
                self.cursor =self.connection.cursor()
                placeholder =""
                for k in kwargs.keys():
                    placeholder +=k + "=%s, "
                placeholder =placeholder.rstrip(" , ")
                query =f"update member set {placeholder}  where id=%s"
                values =[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Data update sucessfully....!")
            else:
                print("No data found....!")
        except Exception as e:
            print(e)    

connection_instance=DbConnect()
print(connection_instance.get_connection())    
        
    
member_instance = GymMemberManagement()
#member_instance.post(name="Manu",place="Kakkand",mobile="9976849335",plan="8 month",fee="8000",joining_date=datetime.today().strftime("%Y-%m-%d"))
member_instance.get()
#member_instance.retrieve(id=1)
#member_instance.delete(id = 5)
member_instance.put(id=4,name="Abhishek",place="Ekm",mobile="9976849367",plan="8 month",fee="9000",joining_date=datetime.today().strftime("%Y-%m-%d"))
