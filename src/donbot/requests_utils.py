import requests


class RequestsUtils:
    @staticmethod
    def send_get_request(url, headers=None, params=None):
        """
        Send a GET request using the requests library.

        :param url: The URL to send the request to.
        :param headers: Optional headers for the request.
        :param params: Optional parameters for the request.
        :return: The response object.
        """
        response = requests.get(url, headers=headers, params=params)
        return response

    @staticmethod
    def send_post_request(url, headers=None, data=None, json=None):
        """
        Send a POST request using the requests library.

        :param url: The URL to send the request to.
        :param headers: Optional headers for the request.
        :param data: Optional data for the request (used for form data).
        :param json: Optional JSON data for the request.
        :return: The response object.
        """
        response = requests.post(url, headers=headers, data=data, json=json)
        return response

    @staticmethod
    def send_put_request(url, headers=None, data=None, json=None):
        """
        Send a PUT request using the requests library.

        :param url: The URL to send the request to.
        :param headers: Optional headers for the request.
        :param data: Optional data for the request (used for form data).
        :param json: Optional JSON data for the request.
        :return: The response object.
        """
        response = requests.put(url, headers=headers, data=data, json=json)
        return response

    @staticmethod
    def send_delete_request(url, headers=None):
        """
        Send a DELETE request using the requests library.

        :param url: The URL to send the request to.
        :param headers: Optional headers for the request.
        :return: The response object.
        """
        response = requests.delete(url, headers=headers)
        return response
