from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "partial/home.html")


def clas(request, id=None):
    return render(request, "partial/clas.html")
