import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.service_type import ServiceType


class Service(db.Model):

    def __init__(self):
        self.__tablename__ = "service"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    model = db.Column(db.String(length=10), nullable=False)
    delivery_mode = db.Column(db.String(length=100), nullable=False)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))

    service_type_id = db.Column(db.BigInteger, db.ForeignKey(ServiceType.id), nullable=False)

    def __repr__(self):
        return "<Service Id %r>" % self.id + \
            "<Service Model %r>" % self.model


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
