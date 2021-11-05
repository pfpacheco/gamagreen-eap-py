import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.metering_type import MeteringType


class Metering(db.Model):

    def __init__(self):
        self.__tablename__ = "metering"

    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    value = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    metering_type_id = db.Column(db.BigInteger, db.ForeignKey(MeteringType.id), nullable=False)

    def __repr__(self):
        return "<Metering Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
