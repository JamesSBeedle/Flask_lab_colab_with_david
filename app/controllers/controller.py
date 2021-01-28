from flask import render_template, request, redirect
from app import app
from app.modules.event_list import events
from app.modules.task import *


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=["POST"])
def add_event():
    event_date = str(request.form["date"])
    event_number_events = request.form["number_of_events"]
    event_number_guests = request.form["guests"]
    event_room = request.form["room"]
    event_description = request.form["description"]
    event_recurring = True if "recurring" in request.form else False 

    new_event = Event(event_date, event_number_events, event_number_guests, event_room, event_description, event_recurring)

    events.append(new_event)
    print("Did This Work", request.form)
    return redirect('/events')
