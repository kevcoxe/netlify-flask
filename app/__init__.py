from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:6egDG6af-DD6aHC6-F3gEEAd1BC-4HEC@roundhouse.proxy.rlwy.net:50355/flask_login'
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
db = SQLAlchemy(app)
