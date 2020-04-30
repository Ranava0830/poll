from django.shortcuts import render
from .models import poll
from django.views.genric import LisView
# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render(req,'poll_list.html',{'poll_list':polls})

