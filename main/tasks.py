import json

from celery import shared_task
from celery.schedules import crontab


def summarize_news(news):
    import requests
    import itertools
    url_list = []
    text_list = []
    for url, text in news:
        text_list.append(text)
        url_list.append(url)

    summary_list = []
    for text in text_list:
        url = "https://api.remarkapp.io/summary"
        data = {"src": text}
        response = requests.post(url, json=data)
        response = json.loads(response.text)
        summary_list.append(list(response.values()))
    summary_list = list(itertools.chain(*summary_list))

    result = dict(zip(url_list, summary_list))

    return result


@shared_task(name='summarize')
def summarize():
    from google.cloud import firestore
    db = firestore.Client(project='glowing-service-274512')
    users_ref = db.collection(u'RedditNews')

    print('hello')
    entertainment = users_ref.document('entertainment').get().to_dict()
    entertainment_summary = summarize_news(list(entertainment['entertainment'].values()))
    print('entertainment done')
    politics = users_ref.document('politics').get().to_dict()
    politics_summary = summarize_news(list(politics['politics'].values()))
    print('politics done')
    technews = users_ref.document('technews').get().to_dict()
    technews_summary = summarize_news(list(technews['TechNews'].values()))
    print('technews done')
    internet = users_ref.document('internetisbeautiful').get().to_dict()
    internet_summary = summarize_news(list(internet['InternetIsBeautiful'].values()))
    print('internet done')
    sport = users_ref.document('sport').get().to_dict()
    sport_summary = summarize_news(list(sport['sport'].values()))
    print('sport done')

    doc_ref = users_ref.document('summary')
    doc_ref.set({"entertainment-summary": entertainment_summary,
                 "politics_summary": politics_summary,
                 "technews_summary": technews_summary,
                 'internet_summary': internet_summary,
                 'sport_summary': sport_summary})





