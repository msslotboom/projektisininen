from database import db


class Citation(db.Model):
    __tablename__ = "citations"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    type = db.Column(db.String)
    given_id = db.Column(db.Integer)
