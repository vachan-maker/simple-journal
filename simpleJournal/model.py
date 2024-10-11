from simpleJournal import db
from datetime import date, datetime
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    textEntry = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"User('{self.id}', '{self.title}', '{self.textEntry}')"