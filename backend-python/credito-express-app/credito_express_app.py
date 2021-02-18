import os
from flask import Flask, Blueprint, request, jsonify, render_template
from flask_cors import CORS
from log import log
from db import config_db, data_init
from bson import json_util
import json

application = Flask(__name__)
CORS(application)

db = config_db(application)
data_init(db)

@application.route('/')
def index():
    log.info('API call index')
    return render_template('index.html')

@application.route('/api/v1/test')
def test():
    log.info('API call test')
    return jsonify(
        status=True,
        message="Ok, It's alive!!"
    )

@application.route('/api/v1/login', methods=['POST'])
def login():
    log.info('API call login')
    data = request.get_json(force=True)
    cpf = data['cpf']
    phone_number = data['phone_number']
    
    if data['cpf'] is not None and data['phone_number'] is not None:
        custumer = db.clientes.find_one({"cpf": cpf, "celular": phone_number})
        if custumer:
            return jsonify(status=True, message='Ok, find custumer')

    return jsonify(status=False, message="no found custumer for cpf: {} and phone number: {}".format(cpf, phone_number))

@application.route('/api/v1/customers', methods=['GET'])
def customers():
    _clientes = db.clientes.find()
     
    data = json.loads( json_util.dumps(_clientes))

    return jsonify(data)

@application.route('/api/v1/loan', methods=['GET'])
def tax():
    _taxas = db.taxas.find()
 
    item = {}
    data = []
    for taxa in _taxas:
        item = {
            'tipo': taxa['tipo'],
            'taxas': taxa['taxas']
        }
        data.append(item)

    return jsonify(data)

@application.route('/api/v1/loan', methods=['POST'])
def loan():
    log.info('API call login')
    data = request.get_json(force=True)
    cpf = data['cpf'] 
    phone_number = data['phone_number']
    loan_value = data['loan_value']
    installments = data['installments']

    if cpf is not None and phone_number is not None:
        custumer = db.clientes.find_one({"cpf": cpf, "celular": phone_number})
        if custumer:
            score = custumer['score']
            negative = custumer['negativado']
            tax_type = 'SCORE_BAIXO'
            
            if negative is True:
                tax_type = 'NEGATIVADO'
            else:
                if int(score) > 500:
                    tax_type = 'SCORE_ALTO'
   
            tax = db.taxas.find_one({"tipo": tax_type})
            if tax:
                taxs = tax['taxas']
                return jsonify(status=True, data=taxs[installments])
    
    return jsonify(status=False, data='Error')

@application.route('/api/v1/simulation', methods=['POST'])
def simulation():
    log.info('API call simulation')
    data = request.get_json(force=True)
    loan_value = float(data['loan_value'])
    tax = float(data['tax'])
    installments = int(data['installments'])

    amount = loan_value * ((1 + tax/100)**installments)
    fees = amount-loan_value

    return jsonify(
        status=True,
        message="Loan value: {}\nFees (Tax: {}): {}\nAmount after ({} months): {}".format(str("R$ %.2f" % loan_value), tax, str("R$ %.2f" % fees), installments, str("R$ %.2f" % amount))
    )

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(application.config['SERVER_NAME']))
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
