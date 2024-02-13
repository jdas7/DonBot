import requests


class RequestsUtils:
    @staticmethod
    def send_get_request(url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response
