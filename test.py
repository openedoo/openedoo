from openedoo import app
import unittest
import json


class MyTestCase(unittest.TestCase):
    def setUp(self):
             app['TESTING'] = True
             self.app = app.test_client()

    def test_json_post(self):
         headers = [('Content-Type', 'application/json')]
         data = {
         	"username":"demo2",
         	"password":"demo2",
         	"email":"demo2@gmail.com",
         	"name":"Demo2",
         	"phone":"0888"
         }
         json_data = json.dumps(data)
         json_data_length = len(json_data)
         headers.append(('Content-Length', json_data_length))
         response = self.app.post('/persons',  data)
