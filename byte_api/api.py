import json
import requests


class Api(object):
    def __init__(self, token, headers=None):
        self.token = token
        self.API_URL = 'https://api.byte.co/'
        if headers:
            self.headers = headers + {'Authorization': token}
        else:
            self.headers = {
                'User-Agent': 'byte/0.2 (co.byte.video; build:145; '
                              'iOS 13.3.0) Alamofire/4.9.1',
                'Authorization': token
            }

    @staticmethod
    def check_response(response):
        if not response:
            raise ValueError('empty response from API, check your token')

    def get(self, url, params=None, check_response=True):
        response = requests.get(self.API_URL + url,
                                params,
                                headers=self.headers).text
        if check_response:
            self.check_response(response)
        return json.loads(response)

    def post(self, url, data=None, json_data=None, check_response=True):
        response = requests.post(self.API_URL + url,
                                 data,
                                 json_data,
                                 headers=self.headers).text
        if check_response:
            self.check_response(response)
        return json.loads(response)

    def put(self, url, data=None, check_response=True):
        response = requests.put(self.API_URL + url,
                                data,
                                headers=self.headers).text
        if check_response:
            self.check_response(response)
        return json.loads(response)

    def delete(self, url, check_response=True):
        response = requests.delete(self.API_URL + url,
                                   headers=self.headers).text
        if check_response:
            self.check_response(response)
        return json.loads(response)
