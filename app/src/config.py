# データベースの接続文字列など、アプリケーションの設定情報の指定
import os


class DevelopmentConfig:

    # MySQL設定
    DB_NAME = os.getenv('DB_DATABASE', 'hoge')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
    DB_PORT = os.getenv('DB_PORT', 3306)

Config = DevelopmentConfig
