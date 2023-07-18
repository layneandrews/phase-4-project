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
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    floors = db.Column(db.Integer)
    garage = db.Column(db.Boolean)
    pool = db.Column(db.Boolean)
    
    # keeps track of when a property is created
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # keeps track of when a property is updated
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Property Address:{self.address}, Image:{self.image}, Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, Floors: {self.floors}, Garage: {self.garage}, Pool: {self.pool}>'

