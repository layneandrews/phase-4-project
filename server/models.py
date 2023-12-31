from ipdb import set_trace
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

# initializes our DB to link up with SQLAlchemy
db = SQLAlchemy()

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
    
    
    # keeps track of when a property is created
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # keeps track of when a property is updated
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # takes tuple of all columns you want to omit
    serialize_rules = ('-created_at', '-updated_at')

    @validates("address", "city", "state")
    def val_location(self, key, value):
        if isinstance(value, str):
            return value
        raise ValueError("Exceeded max characters allowed for address")

    def __repr__(self):
        return f'<Property Address: {self.address}, City: {self.city}, State: {self.state}, Image: {self.image}, Bedrooms: {self.bedrooms}, Bathrooms: {self.bathrooms}, Floors: {self.floors}>'
    
class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"))


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    admin = db.Column(db.String, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    _password_hash = db.Column(db.String)

    serialize_rules = ("-_password_hash","-admin", "-created_at", "-updated_at")


    def __repr__(self):
        return f'USER: ID: {self.id}, Name {self.name}, Email: {self.email}, Admin: {self.admin}'

# class User(db.Model):
#     __tablename__ = 'user'

#     email = db.Column(db.String, primary_key=True)
#     password = db.Column(db.String)
#     authenticated = db.Column(db.Boolean, default=False)

#     def is_active(self):         # JOSEPH'S CODE
#         return True
    
#     def get_id(self):
#         return self.email
    
#     def is_authenticated(self):
#         return self.authenticated
    
#     def is_anonymous(self):
#         return False
