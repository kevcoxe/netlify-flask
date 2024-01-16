from flask import render_template, jsonify, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app
from app.models import db, User, Cliente


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        adm = request.form['adm']

        if (adm == 0) or (adm == 'False') or (adm == 'false'):
            adm = True
        else:
            adm = False

        user = User(name, email, bool(adm), pwd)

        db.session.add(user)
        db.session.commit()


    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/', methods=['POST', 'GET'])
def home():
    users = User.query.all()
    return render_template('home.html', users=users)


@app.route('/cliente/<nome_cliente>')
def cliente(nome_cliente):
    cliente = Cliente.query.filter_by(name=nome_cliente).first()
    return render_template('cliente.html', nome_cliente=nome_cliente, cliente=cliente)


@app.route('/novoCliente', methods=['POST', 'GET'])
def novoCliente():

    if request.method == 'POST':

        name = request.form['name']
        cidade = request.form['cidade']
        profissao = request.form['profissao']
        number = request.form['number']

        user_id = current_user.id

        print(current_user.id)

        client = Cliente(name, number, cidade, profissao, user_id)

        db.session.add(client)
        db.session.commit()


    return render_template('novoCliente.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

