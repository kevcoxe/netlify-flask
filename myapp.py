from flask import Flask, render_template, jsonify
app = Flask(__name__)

stuff = [
    {
        'name': 'Kevin',
        'age': 0000
    }
]


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/api/get/stuff', methods=['GET'])
def api_get_stuff():
    print('getting stuff: {}'.format(stuff))
    return jsonify(stuff)


if __name__ == '__main__':
    app.run(debug=True)

