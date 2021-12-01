from application import db

class Awards(db.Model):
    class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    award_id = db.Column(db.Integer, db.ForeignKey('award.id'), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, defaclass Cities(db.Model):
    