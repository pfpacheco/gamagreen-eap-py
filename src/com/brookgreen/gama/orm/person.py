import pytz
from datetime import datetime
from com.brookgreen.gama.exe.app import db


class Person(db.Model):

    def __init__(self):
        self.__tablename__ = "person"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String(length=255), nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=True)
    is_consumed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<Person Id %r>" % self.id + \
                " - " + "<Person Name %r>" % self.name + \
                " - " + "<Person Email %r>" % self.name + \
                " - " + "<Person Date %r>" % self.creation_dt


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
