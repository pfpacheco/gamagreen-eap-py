import pytz
from datetime import datetime
from com.brookgreen.gama.exe.app import db
from com.brookgreen.gama.orm.user import User


class Approver(db.Model):

    def __init__(self):
        self.__tablename__ = "approver"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    creation_dt = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return "<Approver Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
