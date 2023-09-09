from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', method=['POST'])
def signup_post():
    # validate and add user to database
    return redirect(url_for(auth.login))

@auth.route('/logout')
def logout():
    return render_template('logout.html')
