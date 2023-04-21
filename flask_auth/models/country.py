"""Country model."""
from flask_auth.models.base_model import BaseModel, db
from flask_auth.models.region import Region

class Country(db.Model, BaseModel):
	__tablename__ = "countries"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	code = db.Column(db.String(3), unique=True, nullable=False)
