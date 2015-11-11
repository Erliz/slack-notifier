import os.path
import message
import client
import parsers

if os.path.isfile("settings.py"):
    import settings
else:
    import os
    settings = {
        'webHookUrl': os.environ['SLACK_WEBHOOKURL'],
        'username': os.environ['SLACK_USERNAME'],
        'channel': os.environ['SLACK_CHANNEL'],
        'icon_emoji': os.environ['SLACK_ICON_EMOJI'],
        'icon_url': os.environ['SLACK_ICON_URL']
    }

message = Message()
message.text(parsers.getTopBreakingMadNews())
message.username(settings['username'])
message.channel(settings['channel'])
message.icon_emoji(settings['icon_emoji'])
message.icon_url(settings['icon_url'])

client = Client(settings['webHookUrl'])
client.notify(message)
