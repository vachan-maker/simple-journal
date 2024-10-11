#where we initialise application and bring together components
# tells python this is a package and initialises everything we need for the app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
db = SQLAlchemy(app)
#creating instance of the database

from simpleJournal import routes
#prevent circular import