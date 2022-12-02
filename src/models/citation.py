from database import db


class Citation(db.Model):
    __tablename__ = "citations"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    authors = db.Column(db.Text)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
