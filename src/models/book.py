from database import db

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    given_id = db.Column(db.Integer)
    author = db.Column(db.Text)
    title = db.Column(db.Text)
    journal = db.Column(db.Text)
    type = db.Column(db.String)