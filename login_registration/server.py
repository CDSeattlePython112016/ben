from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'login_demo')

bcrypt = Bcrypt(app)

app.secret_key = 'ihopethisworks'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    errors = []

    query = "SELECT * FROM users WHERE email=:email;"
    data = {'email': request.form['email']}

    user = mysql.query_db(query, data)

    if not request.form['email']:
        errors.append('Please enter an email address.')
    elif not re.match(EMAIL_REGEX, request.form['email']):
        errors.append('Not a valid email.')
    elif user:
        errors.append('Email is already in use.')

    if not request.form['password']:
        errors.append('Please enter a password.')
    elif len(request.form['password']) < 8:
        errors.append('Password must be 8 characters.')
    elif request.form['password'] != request.form['confirm']:
        errors.append('Password and confirm password must match.')

    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'pw_hash': bcrypt.generate_password_hash(request.form['password']),
        }

        session['user_id'] = mysql.query_db(query, data)

        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email=:email;"
    data = {"email": request.form["email"]}

    user = mysql.query_db(query, data)

    if not user:
        flash("User name or password not valid")
        return redirect("/")

    user = user[0]
    
    if bcrypt.check_password_hash(user["password"], request.form["password"]):
        session["user_id"] = user["id"]
        return redirect("/success")
    else:
        flash("User name or password not valid")
        return redirect("/")


@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')

    query = 'SELECT * FROM users WHERE id=:id;'
    data = {'id': session['user_id']}
    user = mysql.query_db(query, data)[0]

    return render_template('success.html', user=user)

@app.route('/logoff')
def logoff():
    session.clear()
    return redirect('/')

app.run(debug=True)
