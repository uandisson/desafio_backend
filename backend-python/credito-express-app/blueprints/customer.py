from werkzeug import secure_filename
from flask import (
    Blueprint, request, jsonify#, current_app, send_from_directory, render_template
)
from flask_restplus import Resource
import json
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime
#from flask_mongoengine import Pagination


from models import Clientes
from log import log
from restplus import api
from serializers import customer_serializer

#async
import asyncio
import threading

customer_blueprint = Blueprint('customer', __name__)

api.init_app(customer_blueprint)

@api.route('/api/v1/login/async')
class CustomerAsyncCollection(Resource):

    def get(self):        
        return jsonify(status=True, message="It's alive!")

    #@api.response(201, 'Login successfully.')    
    @api.expect(customer_serializer)
    def post(self):        
        log.info(f"Function: {threading.current_thread().name}")
        data = request.get_json(force=True)

        loop = asyncio.get_event_loop()        
        result = loop.run_until_complete(getLoginAsync(data))
        
        return result

@api.route('/api/v1/login')
class CustomeLoginrCollection(Resource):

    def get(self):        
        return jsonify(status=True, message="It's alive!")

    @api.expect(customer_serializer)
    def post(self): 
        log.info('API call login')
        data = request.get_json(force=True)
        
        return checkLogin(data)

@api.route('/api/v1/customers')
class CustomeCollection(Resource):
    
    def get(self):        
        log.info('API call get customers')
        #_clientes = Pagination(Clientes.objects, 1, 10)        
        _clientes = Clientes.objects.limit(10)
        
        data = json.loads( _clientes.to_json())

        return jsonify(data)

async def getLoginAsync(data):
    await asyncio.sleep(1)
    return checkLogin(data)

def checkLogin(data):
    cpf = data['cpf']
    phone_number = data['phone_number']
    
    if cpf is not None and phone_number is not None:
        try:
            custumer = Clientes.objects.get(cpf=cpf, celular=phone_number)
            if custumer:
                expires = datetime.timedelta(days=1)
                #access_token = create_access_token(identity=cpf)
                
                tokens = {
                    'access_token': create_access_token(identity=cpf, expires_delta=expires),
                    'refresh_token': create_refresh_token(identity=cpf, expires_delta=expires)
                }

                return jsonify(status=True, message='Ok, find custumer', tokens=tokens)
        except Clientes.DoesNotExist:
            return jsonify(status=False, message="no found custumer for cpf: {} and phone number: {}".format(cpf, phone_number))