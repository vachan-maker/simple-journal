#where we initialise application and bring together components
# tells python this is a package and initialises everything we need for the app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)
#creating instance of the database

from simpleJournal import routes
#prevent circular import

with app.app_context():
    db.create_all()  