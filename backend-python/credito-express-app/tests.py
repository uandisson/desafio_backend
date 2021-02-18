import unittest
import requests

class TestFlaskApi(unittest.TestCase):

   def test(self):
        response = requests.get('http://localhost:5000/api/v1/test')
        self.assertEqual(response.json(), {"status":True, "message":"Ok, It's alive!!" })

if __name__ == '__main__':
    unittest.main()
