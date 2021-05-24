from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to the Meeting planner!")


def date(request):
    return HttpResponse("The page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I am Badhan Sen.")
