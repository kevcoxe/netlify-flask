from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
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
