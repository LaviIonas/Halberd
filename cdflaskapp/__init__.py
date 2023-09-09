from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
