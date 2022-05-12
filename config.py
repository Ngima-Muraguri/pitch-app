import os

class Config:


    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'hezzy'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:access@localhost/elite'
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME='milcahkatze@gmail.com'
    MAIL_PASSWORD='katzengima'
    SUBJECT_PREFIX='elite'
    SENDER_EMAIL='milcahkatze@gmail.com'
    
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:access@localhost/elite'


    DEBUG = True



     
config_options = {
'development':DevConfig,
'production':ProdConfig


}