from lxml import html
import requests

def getTopMoscowNews():
    page = requests.get('https://www.yandex.ru/')
    tree = html.fromstring(page.content)

    rawNews = tree.xpath('//div[@class="b-tabs__block i-hidden"]/ul[@class="b-news-list"]/li[@class="b-news-list__item"]/a[@class="b-link b-link_type_colored"]')

    newsPost = ''
    newsCounter = 1

    for news in rawNews:
        newsPost += str(newsCounter) + '. ' + news.text_content() + "\n"
        newsCounter += 1

    return newsPost

def getTopBreakingMadNews():
    page = requests.get('http://breakingmad.me/ru/comedy/')
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
