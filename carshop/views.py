from http.client import HTTPResponse
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, "index.html")


def shop_register(request):
    return render(request, "shop_registration.html")


def user_register(request):
    return render(request, "user_reg.html")
