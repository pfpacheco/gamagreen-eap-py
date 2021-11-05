import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.asset import Asset
from com.brookgreen.gama.orm.user import User


class UserAsset(db.Model):

    def __init__(self):
        self.__tablename__ = "user_asset"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    permission_type = db.Column(db.String(length=5), nullable=False)
    description = db.Column(db.String(length=255), nullable=True)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id), nullable=False)
    asset_id = db.Column(db.BigInteger, db.ForeignKey(Asset.id), nullable=False)

    def __repr__(self):
        return "<User Id %r>" % self.id \
               + " - " + "<Date %r>" + self.creation_dt.strftime("%m/%d/%Y, %H:%M:%S")


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
