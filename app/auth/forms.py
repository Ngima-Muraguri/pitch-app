from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_login import  current_user
from app.models import User

class Register(FlaskForm):
    #Validate not in database
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Thats username is taken. Please choose a different one")
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:  
            raise ValidationError('That email is taken. Please choose a different one')
        