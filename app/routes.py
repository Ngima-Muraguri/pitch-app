from flask import Flask, render_template, url_for,redirect,flash
from app import app, db, bcrypt
from app.models import User, Pitch
from app.forms import Register,Login, Pitches, Update
import os, secrets
from flask_login import login_user, current_user, logout_user, login_required
from PIL import Image
