import requests
import message

class Client(object):
    """docstring for Client"""
    def __init__(self, url, debug = False):
        self._url = url if len(url) else 'http://localhost'
        self._debug = debug

    def notify(self, message):
        instanceof(message, Message)
        if not self._debug:
            requests.post(self._url, None, message.to_JSON())
        else:
            print("Sending: " + message.to_JSON() + "\n"))
