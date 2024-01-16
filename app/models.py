from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:6egDG6af-DD6aHC6-F3gEEAd1BC-4HEC@roundhouse.proxy.rlwy.net:50355/flask_login'
db = SQLAlchemy(app)

class Stuff(db.Model):
    __tablename__ = 'stuff'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

db.create_all()
