# config.py
import os
CREDENTIALS = ("5491132926224", "8iSIdam50IZqqWjqP9N0pQvwTgk=") # replace with your phone and password
class BaseConfig(object):
    SECRET_KEY = '' #os.environ['SECRET_KEY']
    DEBUG = True  #os.environ['DEBUG']
    MONGODB_DB = '' #os.environ['MONGODB_DB']
    MONGODB_USER = '' #os.environ['MONGODB_USER']
    MONGODB_PASS = '' #os.environ['MONGODB_PASS']
    MONGODB_HOST = '' #os.environ['MONGODB_HOST']
    MONGODB_PORT = '' #os.environ['MONGODB_PORT']
    REDIS_HOST = '' #os.environ['REDIS_HOST']
    REDIS_PORT = '' #os.environ['REDIS_PORT']
    REDIS_DATABASE = '' #os.environ['REDIS_DATABASE']
    PHONE = '' #os.environ['PHONE']
    PASSWORD = '' #os.environ['PASSWORD']

class DevConfig(BaseConfig):
    SECRET_KEY = 'hi'
    DEBUG = True
    MONGODB_DB = 'oneline'
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017
    REDIS_HOST = 'redis' 
    REDIS_PORT = 6379
    REDIS_DATABASE = '0'
    
