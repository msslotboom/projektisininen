from database import db

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    given_id = db.Column(db.Text)
    author = db.Column(db.Text)
    editor = db.Column(db.Text)
    title = db.Column(db.Text)
    publisher = db.Column(db.Text)
    year = db.Column(db.Integer)