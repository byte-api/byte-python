import json
import requests


class ByteApi(object):
    def __init__(self):
        self.API_URL = 'https://api.byte.co/'

    def get(self, url, params=None, **kwargs):
        response = requests.get(self.API_URL + url, params, **kwargs).text
        return json.loads(response)

    def post(self, url, data=None, json_data=None, **kwargs):
        response = requests.post(self.API_URL + url, data, json_data, **kwargs).text
        return json.loads(response)
