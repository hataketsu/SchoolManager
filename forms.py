from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class EditClassRoomForm(FlaskForm):
    capacity = IntegerField("Capacity", validators=[DataRequired(), NumberRange(min=0, max=40)])
    save = SubmitField("Save")
