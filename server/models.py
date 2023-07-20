# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# serializer formats our data
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

# initializes our DB to link up with SQLAlchemy
db = SQLAlchemy()

# this creates a table in our DB

class User(db.model):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True
    
    def get_id(self):
        return self.email
    
    def is_authenticated(self):
        return self.authenticated
    
    def is_anonymous(self):
        return False


class Property(db.Model, SerializerMixin):

    # defines the name of the table
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
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

    # takes tuple of all columns you want to omit
    serialize_rules = ('-created_at', '-updated_at')

    @validates("address", "city", "state")
    def val_location(self, key, value):
        if isinstance(value, str) and len(value) in range(2, 51):
            return value
        raise ValueError("Exceeded max characters allowed for address")

    def __repr__(self):
        return f'<Property Address:{self.address}, City:{self.city}, State:{self.state}, Image:{self.image}, Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, Floors: {self.floors}, Garage: {self.garage}, Pool: {self.pool}>'
    
class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"))


