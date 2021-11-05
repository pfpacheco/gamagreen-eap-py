import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.asset import Asset


class Ancillary(db.Model):

    def __init__(self):
        self.__tablename__ = "ancillary"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    service_type = db.Column(db.String(length=10), nullable=False)
    efa_block = db.Column(db.BigInteger, nullable=False)
    s_period_of_settlement = db.Column(db.BigInteger, nullable=False)
    e_period_of_settlement = db.Column(db.BigInteger, nullable=False)
    required_state_of_charge = db.Column(db.Numeric(precision=2, asdecimal=","), nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    asset_id = db.Column(db.BigInteger, db.ForeignKey(Asset.id), nullable=False)

    def __repr__(self):
        return "<Ancillary Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
