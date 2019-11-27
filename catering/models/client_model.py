
from . import db



class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120),  nullable = False)
    password = db.Column(db.String(120), nullable = False)
    client_name = db.Column(db.String(75), nullable = False)
   


    def __init__(self,email,password,client_name):
        self.email = email
        self.password = password
        self.client_name = client_name
       

    def save (self):
        db.session.add(self)
        db.session.commit()
        return 'client successfully created'

  
    
   

# def create_user( email, password, client_name):
#         new_client = Client(email,password, client_name)
        
#         return new_client.save()



    # def update(self, old, data):
    #     for key, item in data.items():
    #         setattr(old, key, item)
    #     self.modified_at = datetime.utcnow()
    #     db.session.commit()
    #     return old



    