import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.metering import Metering
from com.brookgreen.gama.orm.pricing import Pricing
from com.brookgreen.gama.orm.power_source_type import PowerSourceType


class PowerSource(db.Model):

    def __init__(self):
        self.__tablename__ = "power_source"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    capacity = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=False)
    state_of_charge = db.Column(db.Numeric(precision=2, asdecimal=","), nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    pricing_id = db.Column(db.BigInteger, db.ForeignKey(Pricing.id), nullable=False)
    metering_id = db.Column(db.BigInteger, db.ForeignKey(Metering.id), nullable=False)
    power_source_type_id = db.Column(db.BigInteger, db.ForeignKey(PowerSourceType.id), nullable=False)

    def __repr__(self):
        return "<Power Source Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
