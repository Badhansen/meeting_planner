from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meeting.models import Meeting


def welcome(request):
    return render(request, "webside/welcome.html",
                  {"meeting": Meeting.objects.all()})


def date(request):
    return HttpResponse("The page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I am Badhan Sen.")
