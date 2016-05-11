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

def AddAuthor(request):
    if request.method == "POST":
        input_name = request.POST["name"]

        if request.POST["gender"] == "男":
            input_gender = 0
        input_age = int(request.POST["age"])
        input_email = request.POST["email"]
        input_mobile = request.POST["mobile"]
        models.Author.objects.create(name=input_name, gender = input_gender, age = input_age, email = input_email, mobile=input_mobile)
        return redirect("/")


def AddPublisher(request):
    if request.method == "POST":
        input_name = request.POST["name"]
        input_address = request.POST["address"]
        input_province = request.POST["province"]
        input_city = request.POST["city"]
        input_website = request.POST["website"]
        models.Publisher.objects.create(name=input_name, address=input_address, province=input_province, city=input_city, website=input_website)
        return redirect("/")


def AddBook(request):
    if request.method =="POST":
        input_name = request.POST.get("name")
        input_publisher_id = request.POST.get("publisher_id")
        print(input_publisher_id)
        input_publishertime = request.POST.get("publishertime")
        input_author_ids = request.POST.get("author_ids")
        print(input_author_ids)
        new_book=models.Book(
            name=input_name,
            publisher_id=input_publisher_id,
            publishtime=input_publishertime,
        )
        new_book.save()
        new_book.author.add(*input_author_ids)
        return redirect("/")

