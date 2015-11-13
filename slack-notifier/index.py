import os.path
import json
from parsers import parsers
from time import sleep
from message import *
from client import *

settingFilePath = 'settings.json'
if os.path.isfile(settingFilePath):
    with open(settingFilePath) as rawSettings:
        settings = json.load(rawSettings)
else:
    import os
    settings = {
        'webHookUrl': os.environ['SLACK_WEBHOOKURL'],
        'username': os.environ['SLACK_USERNAME'],
        'channel': os.environ['SLACK_CHANNEL'],
        'icon_emoji': os.environ['SLACK_ICON_EMOJI'],
        'icon_url': os.environ['SLACK_ICON_URL'],
        'parser_name': os.environ['PARSER_NAME'],
        'repeat_delay_sec': os.environ['REPEAT_DELAY_SEC']
    }

message = Message()

if 'username' in settings:
    message.username = settings['username']
if 'channel' in settings:
    message.channel = settings['channel']
if 'icon_emoji' in settings:
    message.icon_emoji = settings['icon_emoji']
if 'icon_url' in settings:
    message.icon_url = settings['icon_url']

client = Client(settings['webHookUrl'])
# sleep(60*60*1)
if 'parser_name' not in settings:
    settings['parser_name'] = 'default'
if settings['parser_name'] not in parsers:
    raise ValueError('Not found parser with name %s' % settings['parser_name'])

while True:
    message.text = parsers[settings['parser_name']]()
    client.notify(message)
    if 'repeat_delay_sec' in settings and settings['repeat_delay_sec'] > 0:
        sleep(settings['repeat_delay_sec'])
    else:
        break
