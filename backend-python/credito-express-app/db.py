import os
from flask_pymongo import PyMongo
import json
from log import log

def config_db(app):
    log.info('>>>>> Starting MongoDB')
    app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
    mongo = PyMongo(app)
    return mongo.db

def data_init(db):
    log.info('>>>>> Import Default Data init... ')
    
    collection_clientes = db['clientes']
    collection_taxas = db['taxas']
    
    log.info('>>>>> {} - {} '.format(collection_clientes.count(), collection_taxas.count()))
    
    if collection_clientes.count() == 0 and collection_taxas.count() == 0:

        with open('data/clientes.json') as f:
            file_data = json.load(f)

        collection_clientes.insert_many(file_data)

        with open('data/taxas.json') as f:
            file_data = json.load(f)

        collection_taxas.insert_many(file_data)

        log.info('>>>>> Import Default Data finished ')
    else:
        log.info('>>>>> Import Default Data already imported ')