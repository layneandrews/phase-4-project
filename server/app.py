from ipdb import set_trace
from flask import Flask, request, make_response, jsonify
# migrations are basically fundamental changes to our DB (ex. DROP TABLE, CREATE TABLE, INSERT, etc.)
from flask_migrate import Migrate
from models import db, Property, User
from flask_restful import Api, Resource
from flask_login import LoginManager




# this is how the Flask app is initialized
# __name__ means main
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# this configures json to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route("/properties")
def index():
    all_props = []
    for prop in Property.query.all():
        prop_dict = dict(
            address=prop.address,
            image=prop.image,
            bedrooms=prop.bedrooms,
            bathrooms=prop.bathrooms,
            floors=prop.floors,
            garage=prop.garage,
            pool=prop.pool,
        )
        all_props.append(prop_dict)
    return all_props

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        
        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        if not url_has_allowed_host_and_scheme(next, request.host):
            return flask.abort(400)
        
        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)







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

# This is practice from lectures 1 and 2 in phase 4

# @app.route("/")
# def index():
#     return "<h1>Hello world</h1>"

# @app.route("/context")
# def context():
#     print(request.host)
#     return f'<h1>Path: {request.path} <br> Host: {request.host}</h1>'

# @app.before_request
# def runs_before():
#     print("this is running BEFORE the request")
    
# @app.after_request
# def runs_after():
#     print("this is running AFTER the request")



if __name__ == '__main__':
    app.run(port=5555, debug=True)