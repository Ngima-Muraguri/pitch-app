from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, Pitch
from app.auth.forms import (Register,Login,Update)
from app.auth.utils import save_picture
auths = Blueprint('users', __name__)



@auths.route('/register', methods=['GET','POST'])
def register():
    form = Register()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #Adds new instance of a user to the databse
    
    if form.validate_on_submit():
        password_encrypt = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_created = User(username=form.username.data,email=form.email.data,password=password_encrypt)
        db.session.add(user_created)
        db.session.commit()
        flash(f"Account created for {form.username.data}")
        return redirect(url_for('users.login'))
    
    #Checks if form has errors