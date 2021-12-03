from application import db

class Awards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    club = db.Column(db.String(20), nullable=False)
    stats = db.Column(db.Integer(), nullable=False)

    players = db.relationship('Player', backref = 'award')    

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    club = db.Column(db.String(20), nullable=False)
    award_id = db.Column(db.Integer(), db.ForeignKey('award.id'), nullable=False)
    stats =  db.Column(db.Integer(), nullable=False)
    