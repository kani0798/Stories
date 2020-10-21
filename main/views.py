from django.shortcuts import render
# from .cron import *
from .tasks import summarize


def story(request):
    return render(request, 'main/index.html')






