from application import db

class Awards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    club = db.column(db.String(20), nullable=False)
    stats = db.column(db.Interger(), nullable=False)

    players = db.relationship('players', backref = 'awards')    

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    club = db.column(db.String(20), nullable=False)
    award_id = db.Column(db.Integer(), db.ForeignKey('award.id') 
    