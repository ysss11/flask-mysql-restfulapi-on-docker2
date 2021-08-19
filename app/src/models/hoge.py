# APIリソースで利用、Flask-Migrateでマイグレーションする際に利用
import uuid
import peewee as pe

from datetime import datetime

from marshmallow import Schema
from flask_marshmallow.fields import fields

from .common import UIDField
from src.database import db


# モデル共通
class BaseModel(pe.Model):
    class Meta:
        database = db


class HogeModel(BaseModel):
    id = UIDField(primary_key=True, default=uuid.uuid4)
    name = pe.CharField(max_length=255, null=False)
    state = pe.CharField(max_length=255, null=False)
    createTime = pe.DateTimeField(null=False, default=datetime.now)
    updateTime = pe.DateTimeField(null=False, default=datetime.now)

    class Meta:
        db_table = 'hoges' # テーブル名を指定

    def __repr__(self):
        return '<HogeModel {}:{}>'.format(self.id, self.name)


class BaseSchema(Schema):
    class Meta:
        model = HogeModel


class HogeSchema(BaseSchema):
    class Meta:
        model = HogeModel

    id = fields.UUID()
    name = fields.String()
    state = fields.String()
    createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
