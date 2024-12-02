from flask import Flask, render_template, request
from markupsafe import Markup
from register import register_user

app = Flask(__name__)

def register_data(fname, lname, age, email, password, confirmPassword):


    # if password != confirmPassword:
    #     return 'Passwords don\'t match'
    
    register_user(fname, lname, age, email, password)
    



@app.route("/")
def home():
    title = 'IS3800 Final Project'
    return render_template('index.html', title = title)

@app.route('/login')
def login():
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
        confirmPassword = request.form.get('confirmPassword')

        register_data(fname, lname, age, email, password, confirmPassword)


    title = 'Register'
    return render_template('register.html', title = title)

if __name__ == "__main__":
    app.run(debug=True)
