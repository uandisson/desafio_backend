import traceback
from log import log
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

api = Api(version='1.0', title='Crédito Express API',
          description='Desafio Backend')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500

@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
