from django.shortcuts import render
from google.cloud import firestore
from .parse import main
from multiprocessing import Pool


def story(request):

    db = firestore.Client()
    users_ref = db.collection(u'RedditNews')
    entertainment = users_ref.document('entertainment').get().to_dict()
    entertainment_news = list(entertainment['entertainment'].values())

    politics = users_ref.document('politics').get().to_dict()
    politics_news = list(politics['politics'].values())

    technews = users_ref.document('technews').get().to_dict()
    technews_news = list(technews['TechNews'].values())

    internet = users_ref.document('internetisbeautiful').get().to_dict()
    internet_news = list(internet['InternetIsBeautiful'].values())

    sport = users_ref.document('sport').get().to_dict()
    sport_news = list(sport['sport'].values())

    return render(request, 'main/index.html', locals())








