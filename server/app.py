from ipdb import set_trace
from flask import Flask, request, make_response, jsonify, abort, session
from flask_migrate import Migrate
from models import db, Property, User, Favorite
from flask_restful import Api, Resource
from flask_login import LoginManager
from werkzeug.exceptions import NotFound
from flask_cors import CORS #cross origins resource sharing
from dotenv import dotenv_values
from flask_bcrypt import Bcrypt

# this is how the Flask app is initialized
# __name__ means main
app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# this configures json to print on indented lines
app.json.compact = False
# ENV = dotenv_values("../.env")
# app.secret_key = ENV["SECRET_KEY"]

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


class Properties(Resource):
    def get(self):
        all_props = [prop.to_dict() for prop in Property.query.all()]
        return make_response(all_props, 200)
    
    def post(self):
        form_json=request.get_json()
        new_prop = Property(
            address=form_json["address"],
            city=form_json["city"],
            state=form_json["state"],
            image=form_json["image"],
            bedrooms=int(form_json["bedrooms"]),
            bathrooms=int(form_json["bathrooms"]),
            floors=int(form_json["floors"]),
            
        )
        db.session.add(new_prop)
        db.session.commit()
        return make_response(new_prop.to_dict(), 201)
    
api.add_resource(Properties, "/properties")

class PropertyById(Resource):
    def get(self, id):
        found_prop = Property.query.filter_by(id=id).first()
        if found_prop:
            return make_response(found_prop.to_dict(), 200)
        else:
            return make_response({"error": f'property { id } not found'}, 404)

    def patch(self, id):
        found_prop = Property.query.filter_by(id=id).first()
        form_data = request.form
        for key in form_data:
            print(f'{key}: {form_data[key]}')
            setattr(found_prop, key, form_data[key])
        db.session.add(found_prop)
        db.session.commit()
        return make_response(found_prop.to_dict(), 200)

    def delete(self, id):
        found_prop = Property.query.filter_by(id=id).first()
        if not found_prop:
            raise abort(404, f'Property of ID: {id} not found')
        db.session.delete(found_prop)
        db.session.commit()
        return make_response({}, 204)
        
        
api.add_resource(PropertyById, "/properties/<int:id>")


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


# login_manager = LoginManager(app)
# login_manager.init_app(app)

# @app.route("/properties")
# def index():
#     all_props = []
#     for prop in Property.query.all():
#         prop_dict = dict(
#             address=prop.address,
#             image=prop.image,
#             bedrooms=prop.bedrooms,
#             bathrooms=prop.bathrooms,
#             floors=prop.floors,
#             garage=prop.garage,
#             pool=prop.pool,
#         )
#         all_props.append(prop_dict)
#     return all_props                    #JOSEPH'S CODE

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         login_user(user)
        
#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         if not url_has_allowed_host_and_scheme(next, request.host):
#             return flask.abort(400)
        
#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)