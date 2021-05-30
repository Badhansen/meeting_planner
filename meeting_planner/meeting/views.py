from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meeting/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meeting/rooms_list.html",
                  {"rooms": Room.objects.all()})


def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meeting/new.html",
                  {"form": form})
