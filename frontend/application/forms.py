from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AwardForm(FlaskForm):
    description = StringField("Award Description", validators=[DataRequired()])
    name = SelectField("Player_Name", choices=[])
    submit = SubmitField("Add Award to a Player")