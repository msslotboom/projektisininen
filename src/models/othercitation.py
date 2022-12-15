from database import db

class OtherCitation(db.Model):
    __tablename__ = "othercitations"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    given_id = db.Column(db.Integer)
    author = db.Column(db.Text)
    title = db.Column(db.Text)
    type = db.Column(db.Text)
    note = db.Column(db.Text)
    year = db.Column(db.Integer)