import crud
from flask import flash, Flask, redirect, render_template, request, session
from jinja2 import StrictUndefined
from model import connect_to_db


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def render_homepage():
    """Renders homepage if a user is logged in"""
    # user_id = session['user_id']
    # if "user_id" in session:
    #     return render_template("home.html")
    # else:
    return redirect('/register')

@app.route('/login', methods=['GET', 'POST'])
def render_login():
    """Logs user in and redirects to homepage"""
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """Logs user in and redirects to homepage"""
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        crud.register_user(username=username, password=password)
        flash('registered!')
    return render_template("registration.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)