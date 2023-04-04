from movieproject import db, app
from movieproject.models import User

with app.app_context():
    userInput = input('Drop of Create?: ')
    if userInput == 'drop':
        db.drop_all()
    if userInput == 'create':
        db.create_all()
    if userInput == 'accountdel':
        users = User.query.all()
        for user in users:
            print(user.id, user.email, user.gebruikersnaam)
        userInput = input('Welk ID wil je verwijderen? : ')
        if userInput != '':
            cursor = User.query.get(int(userInput))
            db.session.delete(cursor)
            db.session.commit()
    else:
        print('\nNothing happened...')
        