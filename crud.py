"""CRUD Function"""
from flask import session
from model import db, User, Reservation
from datetime import date
from sqlalchemy import cast, Date
from werkzeug.security import generate_password_hash, check_password_hash


def check_password(username, password):
    """Checks user password"""
    user = get_user_by_username(username)
    return check_password_hash(user.password_hash, password)


def get_appts_by_user_id(user_id):
    return Reservation.query.filter_by(user_id=user_id).all()

def get_existing_appts(appt_date):
    """Get all appointments booked within time frame user searched"""
    return Reservation.query.filter(cast(Reservation.date, Date)==appt_date).all()

def get_user_by_username(username):
    """Returns user object"""
    return User.query.filter_by(username=username).first()

def register_user(username, password):
    """Registers new user to users table"""
    new_user = User(username=username, password_hash=generate_password_hash(password))
    
    db.session.add(new_user)
    db.session.commit()

    return new_user