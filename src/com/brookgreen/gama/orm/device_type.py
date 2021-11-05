import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db


class DeviceType(db.Model):

    def __init__(self):
        self.__tablename__ = "device"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    type = db.Column(db.String(length=5), nullable=False, index=True)
    description = db.Column(db.String(length=255), nullable=True)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    def __repr__(self):
        return "<Device Type Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
