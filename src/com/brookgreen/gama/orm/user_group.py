import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db


class UserGroup(db.Model):

    def __init__(self):
        self.__tablename__ = "user_group"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    group = db.Column(db.String(length=5), nullable=False, unique=True)
    description = db.Column(db.String(length=255), nullable=True)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=True, default=datetime.now(tz=pytz.timezone("Europe/London")))

    def __repr__(self):
        return "<User Group Id %r>" % self.id \
               + "<User Group %r>" % self.group \
               + "<User Description %r>" % self.description \
               + " - " + "<Date Group %r>" + self.creation_dt.strftime("%m/%d/%Y, %H:%M:%S")


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
