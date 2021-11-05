import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db


class MeteringType(db.Model):

    def __init__(self):
        self.__tablename__ = "metering_type"

    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    type = db.Column(db.String(length=5), nullable=False, index=True)
    unit = db.Column(db.String(length=3), nullable=False)
    description = db.Column(db.String(length=255), nullable=True)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    def __repr__(self):
        return "<Metering Type Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
