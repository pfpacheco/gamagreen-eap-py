import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.user import User
from com.brookgreen.gama.orm.asset import Asset
from com.brookgreen.gama.orm.asset_type import AssetType


class AssetLog(db.Model):

    def __init__(self):
        self.__tablename__ = "asset_log"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    description = db.Column(db.String(length=255), nullable=False)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=pytz.timezone("Europe/London")))

    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id), nullable=False)
    asset_id = db.Column(db.BigInteger, db.ForeignKey(Asset.id), nullable=False)
    asset_type_id = db.Column(db.BigInteger, db.ForeignKey(AssetType.id), nullable=False)

    def __repr__(self):
        return "<AssetLog Id %r>" % self.id


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
