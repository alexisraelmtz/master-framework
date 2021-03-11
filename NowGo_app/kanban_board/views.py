from django.http import HttpResponse
from django.shortcuts import render

# from .models import board, column, house, city


def myTest(request):
    return render(request, "index.html")


def myBoard(request):
    # Product.objects.all() / .filter() / .get() / .save()
    # return HttpResponse("Hello, World!")
    # items = Board.objects.all()
    return render(request, "index.html", {"items": items})


def myHome(request):
    return HttpResponse("New View!\n\n Hello, World!!!")
