import json

class Message(object):
    """docstring for Message"""
    def __init__(self, text = ''):
        self._text = text if len(text) else 'Test message'
        self._channel = '#general'
        self._username = 'slack-notifier'
        self._icon_emoji = ''
        self._icon_url = ''
        pass

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def icon_emoji(self):
        return self._icon_emoji

    @icon_emoji.setter
    def icon_emoji(self, value):
        self._icon_emoji = value

    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value

    def to_JSON(self):
        def default(o):
            jsonDict = {}
            for key, val in o.__dict__.items():
                if val and len(val):
                    jsonDict[key[1:]] = o.__dict__.get(key)
            print(jsonDict)
            return jsonDict
        print(self.__dict__)
        return json.dumps(
            self,
            default = default,
            sort_keys = True,
            indent = 4
        )
