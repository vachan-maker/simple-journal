from flask import render_template,url_for,redirect,request,flash
from simpleJournal import app, db
from simpleJournal.model import JournalEntry
from sqlalchemy.exc import SQLAlchemyError, DBAPIError
from bs4 import BeautifulSoup
import markdown
import random
import pytz
from datetime import datetime

colors = ['light-yellow','light-pink','blue','yellow']


@app.route('/')
def index():
    entries = JournalEntry.query.all()
    for entry in entries:
        markdownText = markdown.markdown(entry.textEntry)
        entry.textEntry = ''.join(BeautifulSoup(markdownText).findAll(text=True))
        color = random.choice(colors)
        entry.color = color

    return render_template('home.html', entries=entries)

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
    print(pytz.country_names['in'])
    print(type(entry.created_at))
    date_time_of_entry = entry.created_at
    utc = pytz.timezone('UTC')
    utc_dateTime = utc.localize(date_time_of_entry)

    ist_zone = pytz.timezone('Asia/Kolkata')
    ist_dateTime = utc_dateTime.astimezone(ist_zone)
    entry.created_at = ist_dateTime.strftime("%a %B %d, %Y at %H:%M")
    print(entry.created_at)
    return render_template('note.html', noteTitle = entry.title, noteContent=markdown.markdown(entry.textEntry),noteDateTime = entry.created_at)

