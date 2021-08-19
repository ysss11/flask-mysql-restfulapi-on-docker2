# データベースを利用するための初期化処理やマイグレーション管理のために必要なメソッドを定義
import inspect
import peewee as pw
from src.config import Config


db = pw.MySQLDatabase(
    database = Config.DB_NAME,
    host = Config.DB_HOST,
    user = Config.DB_USER,
    password = Config.DB_PASSWORD,
    port = Config.DB_PORT,
)

def create_table():
    """ テーブル作成 """
    import src.models as model
    print('start create_table')
    tables = [
        obj for name, obj in inspect.getmembers(
            model,
            lambda obj: isinstance(obj, pw.ModelBase) and issubclass(
                obj, model.BaseModel)
        ) if name != 'BaseModel'
    ]
    db.connect()
    with db.atomic():
        db.create_tables(tables)
    db.close()

    print('end create_table')
