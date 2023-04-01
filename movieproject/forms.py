from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField,
                                  IntegerField, PasswordField)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from movieproject.models import User

class InlogForm(FlaskForm):
    email = StringField('Voer je email in', validators=[DataRequired(), Email()])
    password = PasswordField('Voer je wachtwoordi n', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Voer uw gebruikersnaam in', validators=[DataRequired()])
    email = StringField('voer uw email in', validators=[DataRequired(),Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm',    message='Passwords Must Match!')])
    pass_confirm = PasswordField('Bevestig uw wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Registreren')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd!')
        
    def validate_username(self, field):
        if User.query.filter_by(gebruikersnaam=field.data).first():
            raise ValidationError('Deze gebruikersnaam is al vergeven, probeer een ander naam!')
    
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