from ipdb import set_trace
from flask import Flask, request
# migrations are basically fundamental changes to our DB (ex. DROP TABLE, CREATE TABLE, INSERT, etc.)
from flask_migrate import Migrate
from models import db, Property


# this is how the Flask app is initialized
# __name__ means main
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def index():
    return "<h1>Hello world</h1>"

@app.route("/context")
def context():
    print(request.host)
    return f'<h1>Path: {request.path} <br> Host: {request.host}</h1>'

@app.before_request
def runs_before():
    print("this is running BEFORE the request")
    
@app.after_request
def runs_after():
    print("this is running AFTER the request")



if __name__ == '__main__':
    app.run(port=5000, debug=True)





# order of operations for initializing and setting up flask app/db:
# flask db init (only once)
# repeat as you progress:
    # flask db migrate -m "message"
    # flask db upgrade

# optional: 

# while in server folder:
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5555

# flask run --debug 
# this actually runs app 