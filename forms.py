from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class SearchForm(FlaskForm):
    countryname= StringField('Country or City  Name',validators=[DataRequired()])
    submit= SubmitField('Search')