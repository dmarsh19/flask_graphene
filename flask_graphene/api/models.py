from flask_graphene import db


class Device(db.Model):
    __tablename__ = "devices"
    deviceid = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.Text(50))
    model = db.Column(db.Text(50))
    location = db.Column(db.Text(50))
    readings = db.relationship("Reading", backref="device", lazy=True)


class Reading(db.Model):
    """."""
    __tablename__ = "readings"
    readingid = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.Integer, db.ForeignKey("devices.deviceid"))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    createdatetime = db.Column(db.String(20))

