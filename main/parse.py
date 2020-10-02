from multiprocessing import Pool
import json

import html2text
from readability import Document
import requests


def get_links(url):
    response = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    parsed_json = json.loads(response.text)
    data = parsed_json['data']['children']
    news_url = []
    news_images = []
    for i in data:
        try:
            if i['data']['url_overridden_by_dest'] and i['data']['preview']['images'][0]['source']['url']:
                news_url.append(i['data']['url_overridden_by_dest'])
                news_images.append(i['data']['preview']['images'][0]['source']['url'].replace('amp;', ''))
            else:
                continue
        except KeyError:
            continue
    return news_images[:3], news_url[:3]


def parse_news(news_url):
    response = requests.get(news_url, headers={'User-agent': 'your bot 0.1'})
    doc = Document(response.text)
    doc_title = doc.title()
    h = html2text.HTML2Text()
    h.ignore_links = True
    return f'{doc_title}{h.handle(doc.summary())}'


def speed(url):
    data = parse_news(url)
    return data


def main(url):
    news_images, news_links = get_links(url)
    with Pool(40) as p:
        news_list = p.map(speed, news_links)
    zipped_list = zip(news_images, news_links, news_list)
    # print(list(zipped_list))
    return list(zipped_list)

