import os.path
import requests
from lxml import html

def top_yandex_news():
    page = requests.get('https://www.yandex.ru/')
    tree = html.fromstring(page.content)

    rawNews = tree.xpath('//div[@class="b-tabs__block i-hidden"]/ul[@class="b-news-list"]/li[@class="b-news-list__item"]/a[@class="b-link b-link_type_colored"]')

    newsPost = ''
    newsCounter = 1

    for news in rawNews:
        newsPost += str(newsCounter) + '. ' + news.text_content() + "\n"
        newsCounter += 1

    return newsPost

def top_breakingmad_news():
    page = requests.get('http://breakingmad.me/ru/')
    tree = html.fromstring(page.content)

    rawNews = tree.xpath('//div[@class="news-row"]/h2')

    newsPost = ''
    newsCounter = 1

    for news in rawNews:
        if newsCounter > 5:
            break
        newsPost += str(newsCounter) + '. ' + news.text_content() + "\n"
        newsCounter += 1

    return newsPost

def top_hitech_news():
    page = requests.get('https://hi-tech.mail.ru/news/')
    tree = html.fromstring(page.content)

    rawNewsTitle = tree.xpath('//span[@class="newsitem__title"]')
    rawNewsText = tree.xpath('//span[@class="newsitem__text"]')

    newsPost = ''
    newsCounter = 1

    for news in rawNews:
        if newsCounter > 5:
            break
        newsPost += str(newsCounter) + '. ' + news.text_content() + '. ' + rawNewsText[newsCounter-1] + "\n"
        newsCounter += 1

    return newsPost

def getBashorgComicsByDate(date = ''):
    """date_string have YYYYMMDD string format"""
    if not len(date):
        from time import gmtime, strftime
        date = strftime("%Y%m%d", gmtime())

    page = requests.get('http://bash.im/comics/' + date, allow_redirects = False)

    if page.status_code != 200:
        return ''

    tree = html.fromstring(page.content)
    img = tree.xpath('//div[@id="the_strip"]/img')[0]

    return img.get('src')

def bashorg_comics():
    import json
    from time import sleep

    logPath = 'logs/bashorg_comics_log.json'
    if os.path.isfile(logPath):
        with open(logPath) as logHandler:
            log = json.load(logHandler)
    else:
        log = []

    from datetime import date
    from dateutil.relativedelta import relativedelta
    firstComicsDate = '20070801'
    daysAgo = 0
    formatedDate = ''
    while formatedDate != firstComicsDate:
        formatedDate = str(date.today() - relativedelta(days=daysAgo)).replace('-','')
        daysAgo += 1
        if formatedDate not in log:
            log.append(formatedDate)
            with open(logPath, 'w') as logHandler:
                json.dump(log, logHandler)
            if len(formatedDate):
                comicsSrc = getBashorgComicsByDate(formatedDate)
                if len(comicsSrc):
                    return comicsSrc
                else:
                    sleep(1)


parsers = {
    'default': top_yandex_news,
    'top_yandex_news': top_yandex_news,
    'top_breakingmad_news': top_breakingmad_news,
    'top_hitech_news': top_hitech_news,
    'bashorg_comics': bashorg_comics,
}

customParserModule = 'custom_parsers.py'
if os.path.isfile(customParserModule):
    import customParserModule
    parsers.update(customParserModule.parsers)
