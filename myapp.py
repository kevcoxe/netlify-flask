from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
db = SQLAlchemy(app)


class Stuff(db.Model):
    __tablename__ = 'stuff'

    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

db.create_all()


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/api/get/stuff', methods=['GET'])
def api_get_stuff():
    stuff = [s.json() for s in Stuff.query.all()]
    print('getting stuff: {}'.format(stuff))
    return jsonify(stuff)


@app.route('/api/add/stuff', methods=['POST'])
def api_add_stuff():
    name = request.json.get('name')
    age = request.json.get('age')

    new_stuff = Stuff(
        name=name,
        age=age
    )
    db.session.add(new_stuff)
    db.session.commit()

    print('adding stuff: {}'.format(new_stuff.json()))
    return jsonify(new_stuff.json())


if __name__ == '__main__':
    app.run(debug=True)

