from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateAwardForm(FlaskForm):
    description = 
    name = StringField("Award Name", validators=[DataRequired()])
    player_name = SelectField("Player_Name",
     choices=[
         ('Messi', 'Messi'),
         ('Ronaldo', 'Ronaldo'),
         ('Salah', 'Salah'),
     ])
    submit = SubmitField("Add Award to a Player")