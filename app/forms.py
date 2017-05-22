from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class EncipherForm(FlaskForm):
    input_text = StringField(u'Text to encipher', validators=[DataRequired()])
    numRotations = IntegerField(u'Number Of Rotations', validators=[DataRequired()])
