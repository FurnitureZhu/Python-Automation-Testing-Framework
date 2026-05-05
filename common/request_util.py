import requests
from common.read_yaml import read_yaml

config = read_yaml("config/config.yaml")

class RequestUtil:

    @staticmethod
    def send_request(method, url, **kwargs):
        url = config['base_url'] + url
        response = requests.request(method=method, url=url, **kwargs)
        return response