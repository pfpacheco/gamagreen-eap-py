import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.address_type import AddressType


class Address(db.Model):

    def __init__(self):
        self.__tablename__ = "address"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    lat = db.Column(db.Numeric(precision=6, asdecimal=","), nullable=True)
    lng = db.Column(db.Numeric(precision=6, asdecimal=","), nullable=True)
    line1 = db.Column(db.String(length=255), nullable=False)
    line2 = db.Column(db.String(length=255), nullable=True)
    line3 = db.Column(db.String(length=255), nullable=True)
    city = db.Column(db.String(length=100), nullable=False)
    county_province = db.Column(db.String(length=100), nullable=False)
    zip_or_postcode = db.Column(db.String(length=10), nullable=False)
    country = db.Column(db.String(length=20), nullable=False)
    creation_dt = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=pytz.timezone("Europe/London")))

    address_type_id = db.Column(db.BigInteger, db.ForeignKey(AddressType.id), nullable=False)

    def __repr__(self):
        return "<AssetAddress Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
