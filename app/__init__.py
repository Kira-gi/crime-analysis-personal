import os
from flask import Flask
from app.models import db
from app.routes import register_routes  # Assuming your Blueprints are setup

def create_app():
    
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'), static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))
    app.secret_key = 'cyberguardians'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_BINDS'] = {'crimes': 'sqlite:///crime_data.db'}
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    register_routes(app)

    return app