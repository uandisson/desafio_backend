from restplus import api
from flask_restplus import fields

customer_serializer = api.model('Clientes', {
    'cpf': fields.String(required=True, description='CPF'),
    'phone_number': fields.String(required=True, description='Celular')
})

tax_fields = {
    'id': fields.String,
    'valor': fields.Float,
}

tax_serializer = api.model('Taxas', {
    'tipo': fields.String(description='Tipo'),
    'taxas': fields.List(fields.Nested(tax_fields), description='Número de Parcelas')
})

loan_serializer = api.model('Loan', {    
    'cpf': fields.String(description='CPF'),
    'phone_number': fields.String(description='Celular'),
    'loan_value': fields.String(description='Valor de empréstimo'),
    'installments': fields.String(description='Número de Parcelas') 
})

simulation_serializer = api.model('Simulation', {    
    'tax': fields.String(description='Taxa de Juros'),
    'loan_value': fields.String(description='Valor de empréstimo'),
    'installments': fields.String(description='Número de Parcelas') 
})
