from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField,
                                  IntegerField)
from wtforms.validators import DataRequired

class InlogForm(FlaskForm):
    email = StringField('Voer je e-mail in', validators=[DataRequired()])
    password = StringField('Voer je wachtwoord in', validators=[DataRequired()])

    submit = SubmitField('submit')
    
class RegistratieForm(FlaskForm):
    name = StringField()
    email = StringField()
    password = StringField()
    
    submit = SubmitField('submit')
    
class FilmForm(FlaskForm):
    Titel = StringField()
    Jaar = StringField()
    Genre = StringField()
    Lengte = StringField()
    Description = StringField()
    Rating = StringField()
    Imglink = StringField()
    
    submit = SubmitField('submit')
    
class DeleteForm(FlaskForm):
    id = IntegerField()
    
    submit = SubmitField('submit')