"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table
class Type(enum.Enum):
    Party = 1
    Study = 2
    Networking = 3
    ALL = 4

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    phone = db.Column(db.Integer)
    events_attending = db.relationship(
        "Event", secondary="guest_event", back_populates="guests"
    )

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(140))
    date_and_time = db.Column(db.DateTime)
    event_type = db.Column(db.Enum(Type), default=Type.ALL)
    guests = db.relationship(
        "Guest", secondary="guest_event", back_populates="events_attending"
    )

guest_event_table = db.Table(
    "guest_event",
    db.Column("guest_id", db.Integer, db.ForeignKey("guest.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
)