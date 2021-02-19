import os
from flask_pymongo import PyMongo
import json
from log import log
from flask_mongoengine import MongoEngine

mongoEngineDB = MongoEngine()

#another away
def config_db(app):
    log.info('>>>>> Starting MongoDB')
    app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
    mongo = PyMongo(app)
    return mongo.db