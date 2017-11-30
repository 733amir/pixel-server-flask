from flask import Flask, request, jsonify, render_template, abort
from json import loads as jload
from db import *

app = Flask(__name__)
db = Database()


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/users', methods=['GET'])
def users():
    return jsonify(db.users)


@app.route('/exists', methods=['GET'])
def exists():
    username = request.args.get('username')
    email = request.args.get('email')

    if username is not None and email is None:
        if db.username_exists(username):
            return jsonify({
                'status': 'ok'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Username doesn\'t exists!'
            }), 200  #404
    elif username is None and email is not None:
        if db.email_exists(email):
            return jsonify({
                'status': 'ok'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Email doesn\'t exists!'
            }), 200  #404
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Bad request!'
        }), 200  #400


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    email = request.form['email']

    if None not in [username, password, fullname, email]:
        if db.username_exists(username):
            return jsonify({
                'status': 'error',
                'desc': 'Username exists!'
            }), 200  #403
        elif db.email_exists(email):
            return jsonify({
                'status': 'error',
                'desc': 'Email exists!'
            }), 200  #403
        else:
            db.add_user(username, fullname, email, password)
            return jsonify({
                'status': 'ok'
            }), 200  #201
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Bad request!'
        }), 200  #400


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if None not in [username, password]:
        if db.login(username, password):
            return jsonify({
                'status': 'ok'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Username or Password is wrong!'
            }), 200  #404
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Bad request!'
        }), 200  #400


@app.route('/reset_request', methods=['GET'])
def reset_request():
    email = request.args.get('email')

    if None not in [email]:
        if db.email_exists(email):
            return jsonify({
                'status': 'ok'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Email doesn\'t exists!'
            }), 200  #404
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Bad request!'
        }), 200  #400


@app.route('/reset', methods=['POST'])
def reset():
    email = request.form['email']
    code = request.form['code']
    new_password = request.form['password']

    if None not in [email, code, new_password]:
        if db.get_reset_code(email) == code:
            db.reset_password(email, new_password)
            db.update_reset_code(email)
            return jsonify({
                'status': 'ok'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Email and Code didn\'t match!'
            }), 200  #403
    else:
        return jsonify({
            'status': 'error',
            'desc': 'Bad request!'
        }), 200  #400


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        username = request.args.get('username')
        if None not in [username]:
            if db.username_exists(username):
                return jsonify({
                    'status': 'ok',
                    'profile': db.get_profile(username),
                    'fullname': db.get_user(username)['fullname']
                }), 200
            else:
                return jsonify({
                    'status': 'error',
                    'desc': 'Username doesn\'t exists!'
                }), 200  #404
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Bad request!'
            }), 200  # 400
    elif request.method == 'POST':
        username = request.args.get('username')

        # TODO get header and image of profile.
        fullname = request.form['fullname']
        bio = request.form['bio']
        interests = jload(request.form['interests'])

        user = db.get_user(username)
        user['fullname'] = fullname
        user['profile']['bio'] = bio
        user['profile']['interest'] = interests

        return jsonify({
            'status': 'ok'
        }), 200


@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'GET':
        username = request.args.get('username')
        if None not in [username]:
            if db.username_exists(username):
                email = db.get_email(username)
                return jsonify({
                    'status': 'ok',
                    'account': {
                        'username': username,
                        'email': email
                    }
                }), 200
            else:
                return jsonify({
                    'status': 'error',
                    'desc': 'Username doesn\'t exists!'
                }), 200  # 404
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Bad request!'
            }), 200  # 400
    elif request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        old_password = request.form['old_password']
        new_password = None
        if 'new_password' in request.form:
            new_password = request.form['new_password']

        if None not in [username, email, old_password]:
            user = db.get_user(username)
            if user is not None:
                if user['password'] == old_password:
                    user['email'] = email
                    if new_password is not None:
                        user['password'] = new_password
                    return jsonify({
                        'status': 'ok'
                    }), 200
                else:
                    return jsonify({
                        'status': 'error',
                        'desc': 'Username or Password was wrong!'
                    }), 200  # 403
            else:
                return jsonify({
                    'status': 'error',
                    'desc': 'Username doesn\'t exists!'
                }), 200  # 400
        else:
            return jsonify({
                'status': 'error',
                'desc': 'Bad request!'
            }), 200  # 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
