from requests import get, post
from urllib.parse import quote
import xmltodict
import json


class Url:
    def __init__(self, base_url):
        self.base_url = base_url

    def url_builder(self, action, parameters):
        url = f"{self.base_url}{action}"
        if isinstance(parameters, dict):
            for i in parameters:
                if parameters[i] is not None:
                    url += f"&{i}={quote(parameters[i])}"
        elif isinstance(parameters, str):
            url += parameters

        return url

    def get_url(self, action, parameters=None, cookies=None):
        url = self.url_builder(action, parameters)
        response = get(url, cookies=cookies)
        response.encoding = 'utf-8'
        return json.loads(json.dumps(xmltodict.parse(response.text)))

    def post_url(self, action, parameters=None, cookies=None):
        url = self.url_builder(action, parameters)
        response = post(url, cookies=cookies)
        response.encoding = 'utf-8'
        return json.loads(json.dumps(xmltodict.parse(response.text)))
