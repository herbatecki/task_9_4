from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms import validators
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, NumberRange

class CompactForm(FlaskForm):
    band = StringField('band', validators=[DataRequired()])
    album = StringField('album', validators=[DataRequired()])
    year = IntegerField('year', validators=[NumberRange(min=1950, max=2021)])
    mark = RadioField('mark', choices=[1,2,3,4,5])