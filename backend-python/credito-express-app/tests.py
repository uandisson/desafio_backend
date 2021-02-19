import unittest
import requests

class TestFlaskApi(unittest.TestCase):

    def test(self):
        response = requests.get('http://localhost:5000/api/v1/test')
        self.assertEqual(response.json(), {"status":True, "message":"Ok, It's alive!!" })

    def test_get_tax_check_status_code_equals_200(self):
        response = requests.get("http://localhost:5000/api/v1/tax")
        #assert response.status_code == 200
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
