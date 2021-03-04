from django.http import HttpResponse
from django.shortcuts import render


def myView(request):
    return HttpResponse("Hello, World!")


def newView(request):
    return HttpResponse("New View!\n\n Hello, World!!!")
