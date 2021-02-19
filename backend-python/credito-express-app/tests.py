import unittest
import requests
import json

class TestFlaskApi(unittest.TestCase):
    URL = 'http://localhost:5000/api/v1/'
    headersJson = {'content-type': 'application/json'}
    jsonLoginTestCorrect = {"cpf": "93762814031", "phone_number": "71935228778"}
    jsonLoginTestNone = {"cpf": "", "phone_number": ""}

    def test(self):
        response = requests.get(self.URL + 'test')
        self.assertEqual(response.json(), {"status":True, "message":"Ok, It's alive!!" })

    def test_get_tax_check_status_code_equals_200(self):
        response = requests.get(self.URL + 'tax')
        self.assertEqual(response.status_code, 200)

    def test_post_login_check_status_code_equals_200(self):
        response = requests.post(self.URL + 'login', data=json.dumps(self.jsonLoginTestCorrect), headers=self.headersJson)
        self.assertEqual(response.status_code, 200)

    def test_post_login_async_check_status_code_equals_200(self):
        response = requests.post(self.URL + 'login/async', data=json.dumps(self.jsonLoginTestCorrect), headers=self.headersJson)
        self.assertEqual(response.status_code, 200)
    
    def test_post_login_check_status_error(self):
        response = requests.post(self.URL + 'login', data=json.dumps(self.jsonLoginTestNone), headers=self.headersJson)
        self.assertEqual(response.json()['status'], False)

    def test_post_login_async_check_status_error(self):
        response = requests.post(self.URL + 'login/async', data=json.dumps(self.jsonLoginTestNone), headers=self.headersJson)        
        self.assertEqual(response.json()['status'], False)

    def test_loan_check(self):
        jsonText = {"cpf": "93762814031", "phone_number": "71935228778", "loan_value": "1000", "installments": "6"}
        jsonResult = {
                    "data": 0.04, 
                    "status": True
        }

        response = requests.post(self.URL + 'loan', data=json.dumps(jsonText), headers=self.headersJson)        
        self.assertEqual(response.json(), jsonResult)

    def test_loan_simulation(self):
        jsonText = {"loan_value": "1000.0", "tax": "0.45", "installments": "6"}        
        jsonResult = {
                    "message": "Loan value: R$ 1000.00\nFees (Tax: 0.45): R$ 27.31\nAmount after (6 months): R$ 1027.31", 
                    "status": True
        }

        response = requests.post(self.URL + 'simulation', data=json.dumps(jsonText), headers=self.headersJson)        
        self.assertEqual(response.json(), jsonResult)

if __name__ == '__main__':
    unittest.main()
