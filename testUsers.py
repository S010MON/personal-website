import unittest
import requests
import json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    def test_post_headers_body_json(self):
        url = "http://127.0.0.1:5000/users/"

        # Additional headers.
        headers = {'Content-Type': 'application/json'}

        # Body
        payload = {'key1': 1, 'key2': 'value2'}

        # convert dict to json string by json.dumps() for body data.
        resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

        # Validate response headers and body contents, e.g. status code.
        assert resp.status_code == 200
        resp_body = resp.json()
        assert resp_body['url'] == url

        # print response full body as text
        print(resp.text)


if __name__ == '__main__':
    unittest.main()




