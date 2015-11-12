import requests
from message import *

class Client(object):
    """docstring for Client"""
    def __init__(self, url, debug = False):
        self._url = url if len(url) else 'http://localhost'
        self._debug = debug

    def notify(self, message):
        isinstance(message, Message)
        if not message.text or not len(message.text):
            raise ValueError('Message text is empty')
        jsonMessage = message.to_JSON()
        if not self._debug:
            response = requests.post(self._url, data=jsonMessage)
            print(response.text)
        print("Sending to url:" + self._url + "\nPayload: " + jsonMessage + "\n")
