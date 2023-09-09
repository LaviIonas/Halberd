from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class Events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(20))
    event_time = db.Column(DateTime(timezone=True))
    event_duration = db.Column(db.Float)
    event_status = db.Column(db.Boolean, default=True)

    def __init__(self, name, time, duration, status):
        self.event_name = name
        self.event_time = time
        self.event_duration = duration
        self.event_status = status

    def __repr__(self):
        return '<Event {}>'.format(self.event_name)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
