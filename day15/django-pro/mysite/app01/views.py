from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from app01 import models


# Create your views here.

def login(request):
    if request.method == "POST":
        input_user=request.POST["user"]
        input_pwd=request.POST["pwd"]
        filter_username=models.userinfo.objects.filter(username=input_user)
        if filter_username:
            filter_pwd=models.userinfo.objects.filter(username=input_user).values("password")[0]['password']
            if input_pwd==filter_pwd:
                return redirect("/manager/")
            else:
                return render(request,"login.html",{"log_error":"用户名或者密码错误"},)
        else:
            return render(request,"login.html",{"log_error":"用户名不存在！"},)


    return  render(request,"login.html")

def register(request):

    if request.method == "POST":
        #获取用户输入的账号、密码、手机号等信息
        input_username=request.POST["username"]
        input_pwd=request.POST["pwd"]
        input_phone=request.POST["phone"]
        models.userinfo.objects.create(username=input_username,password=input_pwd,phone=input_phone)
    return  render(request,"register.html")



#后台管理系统
def manager(request):
    return render(request, "manager.html")
