from flask import render_template,url_for,redirect,request,flash
from simpleJournal import app, db
from simpleJournal.model import JournalEntry
from sqlalchemy.exc import SQLAlchemyError, DBAPIError
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entry', methods=["POST"])
def entry():
    try:
        newEntry = JournalEntry(title=str(request.form["title"]),textEntry=str(request.form["text"]))
        db.session.add(newEntry)
        db.session.commit()
    except(SQLAlchemyError, DBAPIError) as e:
        return e

    return redirect(url_for('index'))

