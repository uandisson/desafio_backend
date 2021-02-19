from flask import (
    Blueprint, request, jsonify
)
from flask_restplus import Resource

from log import log
from restplus import api
from serializers import simulation_serializer

simulation_blueprint = Blueprint('simulation', __name__)

api.init_app(simulation_blueprint)

@api.route('/api/v1/simulation')
class SimulationCollection(Resource):

    @api.expect(simulation_serializer)
    def post(self):        
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