from flask import Flask, render_template, request, session, redirect, url_for
from markupsafe import Markup, escape
from db.register import register_user
from db.login import login_user
from db.db import db
from test_input import regex_email, regex_password

app = Flask(__name__)

app.secret_key = 'super_secret'

@app.route('/logout')
def logout():
    session.clear()
    response = redirect(url_for('home'))
    return response

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        logout()
    title = 'IS3800 Final Project'
    message = session.get('email', '')
    return render_template('index.html', title = title, message = message, loggedIn = session.get('loggedIn', False))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not login_user(email, password):
            return render_template(
                'login.html',
                message = "Login credentials not valid.",
                email=email
            )
        else: 
            session['loggedIn'] = True
            session['email'] = email
            return redirect(url_for('home'))

    title = 'Login'
    return render_template('login.html', title = title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirm-password')

        if not regex_email(email):
            return render_template(
                'register.html', 
                message = "Email is not valid",
                fname=fname,
                lname=lname,
                age=age,
                email=email 
            )
        
        if not regex_password(password):
            return render_template(
                'register.html', 
                message = "Password is not strong enough",
                fname=fname,
                lname=lname,
                age=age,
                email=email 
            )

        if password != confirmPassword:
            return render_template(
                'register.html', 
                message = "Password don't match",
                fname=fname,
                lname=lname,
                age=age,
                email=email 
            )

        if register_user(fname, lname, age, email, password):
            session['loggedIn'] = True
            session['email'] = email
            return redirect(url_for('home'))

    title = 'Register'
    return render_template('register.html', title = title)

@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        logout()
    title = 'XSS Prevention'
    return render_template('xss.html', title = title, loggedIn = session.get('loggedIn', False))

@app.route('/xss_bad', methods=['POST'])
def xss_bad():
    comment = request.form['comment']
    return f"{comment}"

@app.route('/xss_good', methods=['POST'])
def xss_good():
    comment = request.form['comment']
    safeComment = escape(comment)
    title = 'XSS Prevention'
    return render_template('xss.html', message=safeComment, title=title, loggedIn = session.get('loggedIn', False))

@app.route('/injection', methods=['GET', 'POST'])
def injection():
    if request.method == 'POST':
        logout()
    title = 'SQL Injection'
    return render_template('injection.html', title = title, loggedIn = session.get('loggedIn', False))

@app.route('/injection_bad', methods=['POST'])
def injection_bad():
    conn, cursor = db()
    email = request.form['email']
    password = request.form['password']
    query = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'"
    result = cursor.execute(query).fetchall()

    print("Query Executed: ", query)
    print("Result: ", result)

    if result:
        message = "Login Successful!"
        response_message = result
        return render_template('injection.html', badmessage=message, response_message = response_message, loggedIn = session.get('loggedIn', False))

    else:
        message = "Invalid Credentials!"
        return render_template('injection.html', badmessage=message, loggedIn = session.get('loggedIn', False))


@app.route('/injection_good', methods=['POST'])
def injection_good():
    conn, cursor = db()
    email = request.form['email']
    password = request.form['password']

    # SELECT * FROM users WHERE email = '' OR '1'='1' AND password = ''
    query = "SELECT * FROM users WHERE email = ? and password = ?"

    result = cursor.execute(query, (email, password)).fetchall()
    if result:
        message = f"Login Successful!"
        return render_template('injection.html', message=message, loggedIn = session.get('loggedIn', False))

    else:
        message = f"Invalid Credentials!"
        return render_template('injection.html', message=message, loggedIn = session.get('loggedIn', False))


if __name__ == "__main__":
    app.run(debug=True)
