import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.contract import Contract
from com.brookgreen.gama.orm.service import Service


class PowerPurchaseAgreement(db.Model):

    def __init__(self):
        self.__tablename__ = "power_purchase_agreement"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    description = db.Column(db.String(length=255), nullable=True)
    s_date = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    e_date = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    contract_id = db.Column(db.BigInteger, db.ForeignKey(Contract.id), nullable=False)
    service_id = db.Column(db.BigInteger, db.ForeignKey(Service.id), nullable=False)

    def __repr__(self):
        return "<PPA Id %r>" % self.id + \
                " - " + "<PPA Start Date %r> " % self.s_date + \
                " - " + "<PPA End Date %r> " % self.e_date


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
