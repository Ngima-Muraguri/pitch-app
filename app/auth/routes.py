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