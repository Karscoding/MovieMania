from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField)
from wtforms.validators import DataRequired

class InlogForm(FlaskForm):
    email = StringField('Voer je e-mail in', validators=[DataRequired()])
    password = StringField('Voer je wachtwoord in', validators=[DataRequired()])

    submit = SubmitField('Verzend')
    
class RegistratieForm(FlaskForm):
    username = StringField()
    email = StringField()
    password = StringField()
    
    submit = SubmitField('Verzend')