from . import db
import uuid
from models.base_model import BaseModel


class UserModel(BaseModel, db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
