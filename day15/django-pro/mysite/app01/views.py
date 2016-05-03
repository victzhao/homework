from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from app01 import models


# Create your views here.

def login(request):
    print(request.method)
    if request.method == "POST":
        input_user=request.POST["user"]
        input_pwd=request.POST["pwd"]
        if input_user=="zhaojianbo" and input_pwd=="zhaojianbo123":

            return redirect("http://www.baidu.com")

        else:
            print("用户名或密码错误！")
            return render(request,"login.html",{"log_error":"用户名或者密码错误"},)
    return  render(request,"login.html")

def register(request):

    if request.method == "POST":
        # user_input = models.userinfo
        # print(user_input)
        print(request.method)
    return  render(request,"register.html")

