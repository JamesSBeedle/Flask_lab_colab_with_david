class Event():
  def __init__(self, date, number_events, number_guests, room, description, recurring=False):
    self.date = date
    self.number_events = number_events
    self.number_guests = number_guests
    self.room = room
    self.description = description
    self.recurring = recurring

