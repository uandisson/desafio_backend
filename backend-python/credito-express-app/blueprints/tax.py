from flask import (
    Blueprint, request, jsonify
)
from flask_restplus import Resource
from bson import json_util
import json

from models import Taxas, Clientes
from log import log
from restplus import api
from serializers import tax_serializer, loan_serializer

tax_blueprint = Blueprint('tax', __name__)

api.init_app(tax_blueprint)

@api.route('/api/v1/tax')
class TaxCollection(Resource):

    def get(self):        
        log.info('API call get tax')
       
        _tax = Taxas.objects.all()
        
        data = json.loads( _tax.to_json())

        return jsonify(data)

@api.route('/api/v1/loan')
class LoanCollection(Resource):
    
    @api.expect(loan_serializer)
    def post(self):        
            log.info('API call loan')
            data = request.get_json(force=True)
            cpf = data['cpf'] 
            phone_number = data['phone_number']
            loan_value = data['loan_value']
            installments = data['installments']

            if cpf is not None and phone_number is not None:
                custumer = Clientes.objects.get(cpf=cpf, celular=phone_number)
                
                if custumer:
                    score = custumer['score']
                    negative = custumer['negativado']
                    tax_type = 'SCORE_BAIXO'
                    
                    if negative is True:
                        tax_type = 'NEGATIVADO'
                    else:
                        if int(score) > 500:
                            tax_type = 'SCORE_ALTO'
        
                    tax = Taxas.objects.get(tipo= tax_type)
                    if tax:
                        taxs = tax['taxas']
                        return jsonify(status=True, data=taxs[installments])
            
            return jsonify(status=False, data='Error')    