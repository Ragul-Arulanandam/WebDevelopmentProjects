from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField
from wtforms.validators import DataRequired



class Dataform(FlaskForm):
    input1 = IntegerField('input1',validators=[DataRequired()])
    input2 = IntegerField('input2',validators=[DataRequired()])
    Results = SubmitField('Results')



