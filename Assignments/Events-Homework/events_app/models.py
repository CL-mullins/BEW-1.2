"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

class Guest(db.Model):
    # - id: primary key
    id = db.Column(db.Integer, primary_key=True)
    # - name: String column
    name = db.Column(db.String)
    # - email: String column
    email = db.Column(db.String)
    # - phone: String column
    phone = db.Column(db.String)
    # - events_attending: relationship to "Event" table with a secondary table
    events_attending = db.relationship('Event', secondary='event_guest', back_populates='guest')



class Event(db.Model):
  # - id: primary key
    id = db.Column(db.Integer, primary_key=True)
    # - title: String column
    title = db.Column(db.String(80), nullable=False)
    # - description: String column
    description = db.Column(db.String(50), nullable=False)
    # - date_and_time: DateTime column
    date_and_time = db.Column(db.DateTime, nullable=False)
    # - guests: relationship to "Guest" table with a secondary table
    num_guests = db.Column(db.Integer, nullable = False)
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')



guest_event_table = db.Table('guest_event',
  # - event_id: Integer column (foreign key)
  db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
  # - guest_id: Integer column (foreign key)
  db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)