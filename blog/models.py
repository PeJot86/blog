from . import db
import datetime

class Entry(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(80), nullable=False)
   body = db.Column(db.Text, nullable=False)
   pub_date = db.Column(db.DateTime, nullable=False,
       default=datetime.datetime.utcnow)
   is_published = db.Column(db.Boolean, default=False)
   comments = db.relationship("Comment", backref="entry", lazy="dynamic")
   


class Comment(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   body = db.Column(db.Text, nullable=False)
   created = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
   is_published = db.Column(db.Boolean, default=False)
   entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
