from django.shortcuts import render

from .parse import main


def story(request):
    entertainment_news = main('https://www.reddit.com/r/entertainment.json')
    entertainment_news = list(entertainment_news)

    sport_news = main('https://www.reddit.com/r/sports.json')
    sport_news = list(sport_news)

    politics_news = main('https://www.reddit.com/r/politics.json')
    politics_news = list(politics_news)

    internet_news = main('https://www.reddit.com/r/InternetIsBeautiful.json')
    internet_news = list(internet_news)

    tech_news = main('https://www.reddit.com/r/technews.json')
    tech_news = list(tech_news)

    return render(request, 'main/index.html', locals())





