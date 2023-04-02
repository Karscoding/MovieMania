from movieproject import db, app
from movieproject.models import User

with app.app_context():
    userInput = input('Drop of Delete?: ')
    if userInput == 'drop':
        db.drop_all()
    if userInput == 'create':
        db.create_all()