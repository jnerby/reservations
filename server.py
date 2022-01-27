import crud
import helpers
from flask import flash, Flask, redirect, render_template, request, session
from jinja2 import StrictUndefined
from model import connect_to_db
from datetime import datetime


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET', 'POST'])
def render_homepage():
    """Renders homepage if a user is logged in"""
    user_id = session['user_id']
    if "user_id" in session:
        return render_template("home.html")
    else:
        return redirect('/login')


@app.route('/search', methods=['GET', 'POST'])
def search_appointments():
    """Searches for user appointments"""
    if request.method == "POST":
        appt_date = datetime.fromisoformat(request.form['appt-date']).date()
        start_time = request.form['start-time']
        end_time = request.form['end-time']

        # Get all appointments booked during user's window
        existing_appts = crud.get_existing_appts(appt_date)

        available_appts = helpers.get_available_appts(existing_appts, appt_date, start_time, end_time)

        return render_template('home.html')
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def render_login():
    """Logs user in and redirects to homepage"""
    session.clear()

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = crud.get_user_by_username(username)

        if user:
            user_id = user.user_id

            if crud.check_password(username, password):
                flash('Welcome!')
                session['user_id'] = user_id
                return redirect('/')
            else:
                flash('Incorrect Password')
        else:
            flash('Invalid username')

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