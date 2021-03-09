from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def myView(request):
    # Product.objects.all() / .filter() / .get() / .save()
    # return HttpResponse("Hello, World!")
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def newView(request):
    return HttpResponse("New View!\n\n Hello, World!!!")
