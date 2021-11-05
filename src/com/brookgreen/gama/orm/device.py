import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.device_type import DeviceType


class Device(db.Model):

    def __init__(self):
        self.__tablename__ = "device"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    simulation = db.Column(db.String(length=50), nullable=False)
    is_enabled = db.Column(db.Boolean, default=True)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    device_type_id = db.Column(db.BigInteger, db.ForeignKey(DeviceType.id), nullable=False)

    def __repr__(self):
        return "<Device Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
