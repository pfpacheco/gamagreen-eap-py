import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.pricing_type import PricingType


class Pricing(db.Model):

    def __init__(self):
        self.__tablename__ = "pricing"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    pricing_type_id = db.Column(db.BigInteger, db.ForeignKey(PricingType.id), nullable=False)

    def __repr__(self):
        return "<Cost Id %r>" % self.id + \
            " - " + "<Cost Value %r>" % self.value


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
