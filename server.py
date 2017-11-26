from flask import Flask, request, jsonify
from db import *

app = Flask(__name__)
db = Database()


@app.route('/')
def root():
    return 'Hello World!'


@app.route('/users', methods=['GET'])
def users():
    return jsonify(db.users)


@app.route('/resets', methods=['GET'])
def resets():
    return jsonify(db.reset_pass_codes)


@app.route('/username_exists', methods=['GET'])
def username_exists():
    username = request.args.get('username')

    # TODO Check username alphanumeric and length and send {'status': 'error'}.

    # Username existence check
    exists = db.username_exists(username)

    if not exists:
        return jsonify({
            'status': 'ok'
        })
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Username exists!'
        })


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return jsonify({
            'status': 'ok',
            'required': [
                {'username': 'string with 5 or more alphanumeric characters.'},
                {'email':    'string with valid email structure.'},
                {'fullname': 'UTF-8 string.'},
                {'password': 'string with 6 or more characters.'}
            ]
        })
    else:
        # TODO check for json structure received and return {'status': 'error'}.
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        email = request.form['email']

        if db.username_exists(username):
            return jsonify({
                'status': 'error',
                'desc': 'username exists!'
            })
        else:
            db.add_user(username, fullname, email, password)
            return jsonify({
                'status': 'ok'
            })


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if db.check(username, password):
        return jsonify({
            'status': 'ok'
        })
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Username or Password is wrong!'
        })


@app.route('/reset_password_request', methods=['GET'])
def reset_password_request():
    email = request.args.get('email')

    if db.email_exists(email):
        db.add_reset_code(email)
        return jsonify({
            'status': 'ok'
        })
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Email doesn\'t exists!'
        })


@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form['email']
    code = request.form['code']
    new_password = request.form['password']

    if db.get_reset_code(email) == code:
        db.reset_password(email, new_password)
        db.remove_reset_code(email)
        return jsonify({
            'status': 'ok'
        })
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Email and Code didn\'t match!'
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
