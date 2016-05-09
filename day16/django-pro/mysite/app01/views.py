from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from app01 import models
import json

# Create your views here.

def BookManager(request):
    return render(request, "child.html")

def AuthManager(request):
    return render(request, "child.html")


def PublsherManager(request):
    return render(request, "child.html")