from typing import MutableMapping
from django.http import HttpResponse
from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):

    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):

    dests = destination.objects.all()
    return render(request, "blog.html", {'dests': dests})

def contact(request):
    return render(request, "contact.html")

def pakages(request):

    dests = destination.objects.all()
    return render(request, "pakages.html", {'dests': dests})



