import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.address import Address
from com.brookgreen.gama.orm.contract import Contract
from com.brookgreen.gama.orm.person import Person


class Provider(db.Model):

    def __init__(self):
        self.__tablename__ = "provider"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    creation_dt = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=pytz.timezone("Europe/London")))

    person_id = db.Column(db.BigInteger, db.ForeignKey(Person.id), nullable=False)
    address_id = db.Column(db.BigInteger, db.ForeignKey(Address.id), nullable=False)
    contract_id = db.Column(db.BigInteger, db.ForeignKey(Contract.id), nullable=False)

    def __repr__(self):
        return "<Provider Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
