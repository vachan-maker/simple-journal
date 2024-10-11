from flask import render_template,url_for,redirect,request
from simpleJournal import app, db
from simpleJournal.model import JournalEntry
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entry', methods=["POST"])
def entry():
    if request.method == "POST":
        newEntry = JournalEntry(id=100,title=str(request.form["title"]),text=str(request.form["text"]))
        db.session.add(newEntry)
        db.session.commit()
    return render_template('index.html')

