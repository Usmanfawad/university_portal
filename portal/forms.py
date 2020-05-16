from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField,IntegerField,widgets
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email,IPAddress,MacAddress
from portal.models import *
from flask_wtf import widgets


class LoginForm(FlaskForm):
    email    = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_email(self,email):
        user = Users.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('This email is not registered.Please register or enter a correct email.')