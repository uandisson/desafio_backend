import os
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db

'''
import json
collection_clientes = db['clientes']
collection_taxas = db['taxas']

with open('data/clientes.json') as f:
    file_data = json.load(f)

collection_clientes.insert_many(file_data)

with open('data/taxas.json') as f:
    file_data = json.load(f)

collection_taxas.insert_many(file_data)
'''



@application.route('/')
def index():
    return render_template('index.html')

@application.route('/test')
def test():
    return jsonify(
        status=True,
        message="Ok, It's alive!!"
    )

@application.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    cpf = data['cpf']
    phone_number = data['phone_number']
    
    if data['cpf'] is not None and data['phone_number'] is not None:
        custumer = db.clientes.find_one({"cpf": cpf, "celular": phone_number})
        if custumer:
            return jsonify(status=True, message='Ok, find custumer')

    return jsonify(status=False, message="no found custumer for cpf: {} and phone number: {}".format(cpf, phone_number))

@application.route('/loan', methods=['POST'])
def loan():
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

@application.route('/simulation', methods=['POST'])
def simulation():
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
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)