# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# initializes our DB to link up with SQLAlchemy
db = SQLAlchemy()

# this creates a table in our DB
class Property(db.Model):
    # defines the name of the table
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    image = db.Column(db.String)

    # keeps track of when a property is created
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # keeps track of when a property is updated
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

