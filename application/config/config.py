class Config(object):
    DB_NAME = "application"

class DevConfig(Config):
    DB_URI = "mysql://root@localhost/" + Config.DB_NAME

class ProdConfig(Config):
    DB_URI = "mysql://someuser:somepass@somehost.com/" + Config.DB_NAME

environments = {
    'dev': DevConfig,
    'prod': ProdConfig
}
