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

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}")
    #Renders the register page 
    
    return render_template('register.html', form=form)

#Login route

@auths.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form  = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@auths.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = Update()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('users.account'))
    image_file = url_for('static',filename=f'images/{current_user.image_file}')
    return render_template('account.html', image=image_file, form=form)

#route logout
@auths.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))