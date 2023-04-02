from movieproject import db, app
from movieproject.models import User

with app.app_context():
    db.create_all()