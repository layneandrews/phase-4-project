from ipdb import set_trace
from flask import Flask, request, make_response, jsonify, abort
# migrations are basically fundamental changes to our DB (ex. DROP TABLE, CREATE TABLE, INSERT, etc.)
from flask_migrate import Migrate
from models import db, Property, User
from flask_restful import Api, Resource
from flask_login import LoginManager



# from werkzeug.exceptions import NotFound



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





api = Api(app)


class Properties(Resource):
    def get(self):
        all_props = [prop.to_dict() for prop in Property.query.all()]
        return make_response(all_props, 200)
    
    def post(self):
        new_prop = Property(
            address=request.form["address"],
            image=request.form["image"],
            bedrooms=int(request.form["bedrooms"]),
            bathrooms=int(request.form["bathrooms"]),
            floors=int(request.form["floors"]),
            garage=True if request.form["garage"] == 'true' else False,
            pool=True if request.form["pool"] == 'true' else False,
        )
        db.session.add(new_prop)
        db.session.commit()
        return make_response(new_prop.to_dict(), 201)
    
api.add_resource(Properties, "/properties")

class PropertyById(Resource):
    def get(self, prop_id):
        found_prop = Property.query.filter_by(id=prop_id).first()
        if found_prop:
            return make_response(found_prop.to_dict(), 200)
        else:
            return make_response({"error": f'property {prop_id } not found'}, 404)

    def patch(self, prop_id):
        found_prop = Property.query.filter_by(id=prop_id).first()
        form_data = request.form
        for key in form_data:
            print(f'{key}: {form_data[key]}')
            setattr(found_prop, key, form_data[key])
        db.session.add(found_prop)
        db.session.commit()
        return make_response(found_prop.to_dict(), 200)

    def delete(self, prop_id):
        found_prop = Property.query.filter_by(id=prop_id).first()
        if not found_prop:
            raise abort(404, f'Property of ID: {prop_id} not found')
        db.session.delete(found_prop)
        db.session.commit()
        return make_response({}, 204)
        
        
api.add_resource(PropertyById, "/properties/<int:prop_id>")


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