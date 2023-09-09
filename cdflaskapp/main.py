from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import User, Event
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    events = Event.query.all()
    return render_template('profile.html',
                            name=current_user.name,
                            events=events)

@main.route('/add_event', methods=['POST'])
@login_required
def add_event():
    name = request.form.get('event_name')
    # time = request.form.get('event_time')
    # duration = request.form.get('event_duration')
    # status = request.form.get('event_status')

    new_event = Event(user_id=current_user.id,
                      name=name)

    db.session.add(new_event)
    db.session.commit()

    return redirect('/profile')
