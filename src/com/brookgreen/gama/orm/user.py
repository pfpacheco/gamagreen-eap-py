import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.person import Person
from com.brookgreen.gama.orm.user_group import UserGroup


class User(db.Model):

    def __init__(self):
        self.__tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    pw_hash = db.Column(db.String(length=32), nullable=False)
    incorrect_password_trials = db.Column(db.SmallInteger, nullable=False)
    is_allowed = db.Column(db.Boolean, nullable=False, default=False)
    is_not_first_access = db.Column(db.Boolean, nullable=False, default=True)
    is_employee = db.Column(db.Boolean, nullable=False, default=True)
    is_approved = db.Column(db.Boolean, nullable=False, default=False)
    is_reproved = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=True)

    person_id = db.Column(db.BigInteger, db.ForeignKey(Person.id), nullable=False)
    user_group_id = db.Column(db.BigInteger, db.ForeignKey(UserGroup.id), nullable=False)

    def __repr__(self):
        return "<User Id %r>" % self.id \
               + " - " + "<Date %r>" + self.creation_dt.strftime("%m/%d/%Y, %H:%M:%S")


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
