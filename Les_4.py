from pprint import pprint
from lxml import html
import requests
from pymongo import MongoClient

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}


# Для мейла
def mail_news():
    mail = 'https://news.mail.ru'
    response_mail = requests.get(mail, headers=header)
    dom_mail = html.fromstring(response_mail.text)
    link_news_mail = dom_mail.xpath(
        "//li[@class='list__item']/a | //li[@class='list__item hidden_medium hidden_large']/a")
    list_of_news = []
    list_of_links = []
    for i in link_news_mail:
        item = {}
        name_news = i.xpath(".//text()")
        a = i.xpath(".//@href")
        full_link = mail + a[0]
        item['news'] = name_news
        item['url'] = full_link
        list_of_news.append(item)
        list_of_links.append(item['url'])
    list_of_source_and_date = []
    list_of_dates = []
    for l in list_of_links:
        item = {}
        r = requests.get(l, headers=header)
        dom_source_and_date = html.fromstring(r.text)
        source = dom_source_and_date.xpath("//div//span[@class='note']/a/@href")
        date = dom_source_and_date.xpath("//div//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
        item['date'] = date
        item['source'] = source
        list_of_source_and_date.append(item)
    for i in list_of_source_and_date:
        for a in list_of_news:
            a["date"] = i["date"]
            a["source"] = i["source"]
    return list_of_news


# mail_news()
# client = MongoClient("192.168.0.107", 27017)
# db = client["news"]
# news_from_mail = db.news_from_mail
# news_from_mail.insert_many(mail_news)

# Для яндекса
def yandex_news():
    main_link = "https://yandex.ru"
    yandex_news = 'https://yandex.ru/news'
    response_yandex = requests.get(yandex_news, headers=header)
    dom_yandex = html.fromstring(response_yandex.text)
    link_news_yandex = dom_yandex.xpath(".//div//h2[@class='story__title']//a")
    source_and_time = dom_yandex.xpath(".//div[@class='story__date']/text()")
    list_of_news = []
    for i in link_news_yandex:
        item = {}
        name_news = i.xpath(".//text()")
        a = i.xpath(".//@href")
        full_link = main_link + a[0]
        item['news'] = name_news
        item['url'] = full_link
        list_of_news.append(item)
    a = 0
    for i in list_of_news:
        i["source and time"] = source_and_time[a]
        a += 1
    return list_of_news

# yandex_news()
# client = MongoClient("192.168.0.107", 27017)
# db = client["news"]
# news_from_yandex = db.news_from_yandex
# news_from_yandex.insert_many(yandex_news())




