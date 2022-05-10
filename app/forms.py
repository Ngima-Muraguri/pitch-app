from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError 
from flask_wtf.file import FileField, FileAllowed
from app.models import User, Pitch