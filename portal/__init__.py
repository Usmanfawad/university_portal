from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "c96418b075871ec41adaea54fee6f4ac"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # function name of our route like url_for
login_manager.login_message_category = 'info'  # bootstrap class

from portal import routes