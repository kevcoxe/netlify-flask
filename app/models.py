from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_login import UserMixin

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    adm = db.Column(db.Boolean, nullable=False)
    clientes = db.relationship('Cliente', backref='user')

    def __init__(self, name, email, adm: bool, password):
        self.name = name
        self.email = email
        self.adm = adm
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
    
    def is_adm(self):
        return self.adm

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    numero = db.Column(db.String(84), nullable=False, unique=True)
    cidade = db.Column(db.String(84), nullable=False)
    profissao = db.Column(db.String(84), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __init__(self, name, numero, cidade, profissao, user_id):
        self.name = name
        self.numero = numero
        self.cidade = cidade
        self.profissao = profissao
        self.user_id = user_id

db.create_all()
