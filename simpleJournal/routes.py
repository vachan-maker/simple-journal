from flask import render_template,url_for,redirect,request,flash
from simpleJournal import app, db
from simpleJournal.model import JournalEntry
from sqlalchemy.exc import SQLAlchemyError, DBAPIError
from bs4 import BeautifulSoup
import markdown
@app.route('/')
def index():
    entries = JournalEntry.query.all()
    for entry in entries:
        markdownText = markdown.markdown(entry.textEntry)
        entry.textEntry = ''.join(BeautifulSoup(markdownText).findAll(text=True))
    return render_template('index.html', entries=entries)

@app.route('/entry', methods=["POST"])
def entry():
    try:
        newEntry = JournalEntry(title=str(request.form["title"]),textEntry=str(request.form["text"]))
        db.session.add(newEntry)
        db.session.commit()
    except(SQLAlchemyError, DBAPIError) as e:
        return e
    return redirect(url_for('index'))
@app.route('/note/<int:id>')
def getEntry(id):
    entry = JournalEntry.query.get_or_404(id)
    return render_template('note.html', noteTitle = entry.title, noteContent=markdown.markdown(entry.textEntry))

