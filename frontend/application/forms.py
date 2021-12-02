from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateAwardForm(FlaskForm):
    award = StringField("Award Name", validators=[DataRequired()])
    name = StringField("Award Player", validators=[DataRequired()]),
    club = SelectField("Award Club", validators=[DataRequired()]),
    stats = StringField("Award Stats", validators=[DataRequired()],
    
    choices=[
        ('Best player'), ('Best player')
        ('Topscorer', 'Topscorer'),
        ('Most asist', 'Most asist'),
    ])
    submit = SubmitField("Add Award ")

class CreatePlayerForm(FlaskForm):
    name = StringField("Player Name", validators=[DataRequired()]),
    club = SelectField("Player Club", validators=[DataRequired()]),
    stats = StringField("Player Stats", validators=[DataRequired()], choices[])
    
    submit = SubmitField("Add Player")