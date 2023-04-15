from movieproject import db, app
from movieproject.models import User

with app.app_context():
    userInput = input('Drop of Create?: ')
    #Database Droppen
    if userInput == 'drop':
        db.drop_all()
    #Database Maken
    elif userInput == 'create':
        db.create_all()
    #Accounts deleten
    elif userInput == 'accountdel':
        users = User.query.all()
        for user in users:
            print(user.id, user.email, user.gebruikersnaam)
        userInput = input('Welk ID wil je verwijderen? : ')
        if userInput != '':
            cursor = User.query.get(int(userInput))
            db.session.delete(cursor)
            db.session.commit()
    #Admin toevoegen
    elif userInput == 'addadmin':
        users = User.query.all()
        for user in users:
            print(user.id, user.email, user.gebruikersnaam, user.user_role)
        userInput = input('Welk ID wil je permissions beheren')
        if userInput != '':
            cursor = User.query.get(int(userInput))
            userInput = input('1 voor Admin, 2 voor User')
            if userInput == '1':
                cursor.user_role = 'Admin'
            else:
                cursor.user_role = 'User'
            db.session.commit()
    else:
        print('\nNothing happened...')
        