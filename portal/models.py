from portal import db, login_manager, app
from sqlalchemy import ForeignKey
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=False)
    password = db.Column(db.String(50), nullable=False, default="123")
    department= db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        return "USER({},{},{},{},{},{},{},{},{},{})".format(self.id, self.fname, self.lname, self.email, self.password, self.department, self.role)


class Semester(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "SEMESTER({},{})".format(self.id, self.name)


class Department(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(30), nullable=False)



class Course(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(30), nullable=False)
