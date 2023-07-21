from app import app
from models import db, Property, Favorite, User
from faker import Faker

# db.init_app(app)

with app.app_context():
    
    print("Deleting tables...")
    Property.query.delete()


    p1 = Property(address="1656 E 1700 N", city="Albequerqeue", state="NM", image="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/80ff523f-ff84-457d-a547-464588d3a3d3/dfkhf07-239ec164-192d-4d66-95a6-ccdd94cfe606.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzgwZmY1MjNmLWZmODQtNDU3ZC1hNTQ3LTQ2NDU4OGQzYTNkM1wvZGZraGYwNy0yMzllYzE2NC0xOTJkLTRkNjYtOTVhNi1jY2RkOTRjZmU2MDYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.KYXTbIzk3yON7PW6J2_HjNNqFwgLC6IPDU3_mz4ylrc", bedrooms=4, bathrooms=3, floors=2)
    db.session.add(p1)
    p2 = Property(address="838 Mt. Rd", city="Logan", state="UT", image="https://t3.ftcdn.net/jpg/01/62/06/40/360_F_162064034_HI2YEgV7km3HMy0rccQczKH2vvpI4OnB.jpg", bedrooms=6, bathrooms=3, floors=2)
    db.session.add(p2)
    p3 = Property(address="123 E 200 N", city="Welsh", state="WV", image="https://media.istockphoto.com/id/1436217023/photo/exterior-of-a-blue-suburban-home.jpg?s=170667a&w=0&k=20&c=nCVY3g1t4Iz17Zs1PU46LDbp7IGEPjXUbMI8RTKsSrc=", bedrooms=4, bathrooms=2, floors=3)
    db.session.add(p3)
    
    db.session.commit()

    print("Properties seeded...")
    

    