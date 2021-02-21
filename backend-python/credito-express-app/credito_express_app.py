import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from log import log
from db import mongoEngineDB, config_db
from db_import_default import data_init

from blueprints.customer import customer_blueprint
from blueprints.tax import tax_blueprint
from blueprints.simulation import simulation_blueprint
from blueprints.default import default_blueprint

application = Flask(__name__)
CORS(application)
jwt = JWTManager(application)

#with config Docker - another way
db = config_db(application)
data_init(db)

application.config.from_pyfile('config.cfg')

application.register_blueprint(customer_blueprint)
application.register_blueprint(tax_blueprint)
application.register_blueprint(simulation_blueprint)
application.register_blueprint(default_blueprint)

mongoEngineDB.init_app(application)

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(application.config['SERVER_NAME']))
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
