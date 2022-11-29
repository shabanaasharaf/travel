from django.shortcuts import render
from django.http import HttpResponse
from .models import travelinfo, team_info


# # Create your views here.
def display(request):
    object=travelinfo.objects.all()
    object1=team_info.objects.all()
    return render(request,"index.html",{'result':object,'output':object1})
