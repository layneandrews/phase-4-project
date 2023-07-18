from app import app
from models import db, Property
from faker import Faker

# db.init_app(app)

with app.app_context():
    
    print("Deleting tables...")
    Property.query.delete()


    p1 = Property(address="1656 E 1700 N", image="image1.png")
    db.session.add(p1)
    p2 = Property(address="838 Mt. Rd", image="image2.png")
    db.session.add(p2)
    p3 = Property(address="123 E 200 N", image="image3.png")
    db.session.add(p3)
    
    db.session.commit()

    print("Properties seeded...")
    

    