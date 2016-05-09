from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from app01 import models
import json

# Create your views here.

def BookManager(request):
    dataDic=models.Author.objects.all()
    print(dataDic)
    return render(request, "index.html", {"dataDic": dataDic})

def AuthManager(request):
    return render(request, "index.html")

def CreateAuthor(request):
    if request.method == "POST":
        ret = {"status": True, "error": ""}
        try:
            RecvData = json.loads(request.POST.get("data"))
            models.Author.objects.create(**RecvData)
        except Exception as e:
            ret["status"] = False
            ret["error"] = str(e)
        return HttpResponse(json.dumps(ret))



def PublsherManager(request):
    return render(request, "index.html")