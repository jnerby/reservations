from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri="postgresql:///reservations", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

class User(db.Model):
    """A User"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String(25))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User username={self.username}"


class Reservation(db.Model):
    """A Reservation"""

    __tablename__ = "reservations"

    res_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Reservation user_id={self.user_id} date={self.date}"
        
if __name__ == "__main__":
    from server import app
    connect_to_db(app)
