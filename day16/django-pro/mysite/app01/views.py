from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from app01 import models
import json

# Create your views here.

def BookManager(request):
    BookDic = models.Book.objects.all()
    AuthorDic = models.Author.objects.all()
    PublisherDic = models.Publisher.objects.all()
    return render(request, "index.html", {"BookDic": BookDic, "AuthorDic": AuthorDic, "PublisherDic": PublisherDic})

def AuthManager(request):
    return render(request, "index.html")

def CreateAuthor(request):
    if request.method == "POST":
        ret = {"status": True, "error": "", "id": ""}
        RecvData = json.loads(request.POST.get("data"))

        try:
            models.Author.objects.create(**RecvData)
            AddId = models.Author.objects.filter(**RecvData).values("id")[0]["id"]
            ret["id"]=AddId
        except Exception as e:
            ret["status"] = False
            ret["error"] = str(e)
        redirect("/CreateAuthor/")
        return HttpResponse(json.dumps(ret))
def DeleteAuthor(request):
    if request.method == "POST":
        ret = {"status": True, "error": ""}
        try:
            RecvData = json.loads(request.POST.get("data"))
            for i in RecvData:
                models.Author.objects.filter(id=int(i)).delete()
        except Exception as e:
            ret["status"] = False
            ret["error"] = str(e)
        return HttpResponse(json.dumps(ret))

def PublsherManager(request):
    return render(request, "index.html")