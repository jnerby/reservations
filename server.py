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


@app.route('/appts')
def show_user_appts():
    """Shows users current appointments"""
    user_id = session['user_id']
    user_appts = crud.get_appts_by_user_id(user_id)
    return render_template("my_appts.html", user_appts=user_appts)


@app.route('/book-appt', methods=['POST'])
def book_appointment():
    """Add appointment booking to db"""
    appt_time = request.json.get('appt_time')
    user_id = session['user_id']
    crud.book_appt(user_id, appt_time)
    
    return 'Booked'


@app.route('/search', methods=['GET', 'POST'])
def search_appointments():
    """Searches for user appointments"""
    if request.method == "POST":
        # get and format appointment date
        appt_date = datetime.fromisoformat(request.form['appt-date']).date()
        
        start_time = datetime.strptime('09:00', '%H:%M').time()
        end_time = datetime.strptime('18:00', '%H:%M').time()
        if request.form['start-time']:
            start_time = datetime.strptime(request.form['start-time'], '%H:%M').time()
        if request.form['end-time']:
            end_time = datetime.strptime(request.form['end-time'], '%H:%M').time()

        # Get all appointments booked during user's window
        existing_appts = crud.get_existing_appts(appt_date)

        # get all available time slots
        available_appts = helpers.get_available_appts(existing_appts, appt_date, start_time=start_time, end_time=end_time)

        return render_template('results.html', available_appts=available_appts)

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