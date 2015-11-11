class Message(object):
    """docstring for Message"""
    def __init__(self, text):
        self._text = text if len(text) else 'Test message'
        self._channel = '#general'
        self._username = 'slack-notifier'
        self._icon_emoji = ''
        self._icon_url = ''

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        return self

    @property
    def channel(self):
        return self._channel

    @text.setter
    def channel(self, channel):
        self._channel = channel
        return self

    @property
    def username(self):
        return self._username

    @text.username
    def username(self, username):
        self._username = username
        return self

    @property
    def icon_emoji(self):
        return self._icon_emoji

    @icon_emoji.setter
    def text(self, icon_emoji):
        self._icon_emoji = icon_emoji
        return self

    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def text(self, icon_url):
        self._icon_url = icon_url
        return self

    def to_JSON(self):
        return json.dumps(
            self,
            default = lambda o: o.__dict__,
            sort_keys = True,
            indent = 4
        )
