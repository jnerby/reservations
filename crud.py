"""CRUD Function"""
from flask import session
from model import db, User, Reservation
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(username, password):
    new_user = User(username=username, password_hash=generate_password_hash(password))
    
    db.session.add(new_user)
    db.session.commit()

    return new_user