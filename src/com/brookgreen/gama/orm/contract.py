import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.contract_type import ContractType


class Contract(db.Model):

    def __init__(self):
        self.__tablename__ = "contract"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    s_date = db.Column(db.DateTime, nullable=False)
    e_date = db.Column(db.DateTime, nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    contract_type_id = db.Column(db.BigInteger, db.ForeignKey(ContractType.id), nullable=False)

    def __repr__(self):
        return "<Contract Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
