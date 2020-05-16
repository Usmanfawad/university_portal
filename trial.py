
from portal.models import *


user_1= Users(f_name="Usman",l_name="Fawad",email="usman@gmail.com",password="123",department="ADMIN",role="ADMIN")
user_2= Users(f_name="Rafay",l_name="abdul",email="rafay@gmail.com",password="123",department="ADMIN",role="ADMIN")


db.session.add(user_2)
db.session.commit()