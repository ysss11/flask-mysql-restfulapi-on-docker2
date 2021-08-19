# 全DBモデルにて共通に利用する親クラス、型など定義
import uuid
from peewee import (
    UUIDField
)

class UIDField(UUIDField):
    """ uid型 デフォルトだとuuidに 「-」が入らないため、変更している """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = uuid.uuid4

    def db_value(self, value):
        """ convert UUID to str """
        return str(value)

    def python_value(self, value):
        """ convert str to UUID """
        if value:
            try:
                return uuid.UUID(value)
            except Exception as e:
                print(f"UUID形式エラー：{value}")
                raise e
        return value
