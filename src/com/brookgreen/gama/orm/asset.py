import pytz

from datetime import datetime

from com.brookgreen.gama.exe.app import db

from com.brookgreen.gama.orm.address import Address
from com.brookgreen.gama.orm.asset_type import AssetType
from com.brookgreen.gama.orm.power_source import PowerSource
from com.brookgreen.gama.orm.device import Device
from com.brookgreen.gama.orm.power_purchase_agreement import PowerPurchaseAgreement


class Asset(db.Model):

    def __init__(self):
        self.__tablename__ = "asset"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(length=80), nullable=False)
    code = db.Column(db.String(length=80), nullable=False, index=True)
    description = db.Column(db.String(length=255), nullable=True)
    control_system = db.Column(db.String(length=50), nullable=False)
    telemetry_data_source = db.Column(db.String(length=50), nullable=False)
    balancing_mechanism = db.Column(db.String(length=100), nullable=True)
    is_balancing_using_schedule = db.Column(db.Boolean, nullable=False)
    ancillary_service = db.Column(db.String(length=100), nullable=True)
    efficiency = db.Column(db.Numeric(precision=2, asdecimal=","), nullable=True)
    max_import_rate = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=True)
    max_export_rate = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=True)
    transmission_loss_multiplier = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=True)
    creation_dt = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    last_update = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone("Europe/London")))
    is_costs_and_revenues_applicable = db.Column(db.Boolean, default=False)
    parasitic_load = db.Column(db.Numeric(precision=5, asdecimal=","), nullable=True)

    device_id = db.Column(db.BigInteger, db.ForeignKey(Device.id), nullable=False)
    address_id = db.Column(db.BigInteger, db.ForeignKey(Address.id), nullable=False)
    asset_type_id = db.Column(db.BigInteger, db.ForeignKey(AssetType.id), nullable=False)
    power_source_id = db.Column(db.BigInteger, db.ForeignKey(PowerSource.id), nullable=False)
    power_purchase_agreement_id = db.Column(db.BigInteger, db.ForeignKey(PowerPurchaseAgreement.id), nullable=False)

    def __repr__(self):
        return "<Asset Id %r>" % self.id + \
                " - " + "<Asset Name %r>" % self.name + \
                " - " + "<Asset Code %r>" % self.code


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
