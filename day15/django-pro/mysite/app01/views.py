from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from app01 import models
import json

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
def save_host(request):
    if request.method=="POST":
        input_hostname=request.POST["hostname"]
        input_ip=request.POST["ip"]
        input_port=request.POST["port"]
        input_cpu=request.POST["cpu"]
        input_mem=request.POST["mem"]
        input_disk=request.POST["disk"]
        input_status=request.POST["status"]
        models.hostinfo.objects.create(hostname=input_hostname,ip=input_ip,port=input_port,cpu=input_cpu,mem=input_mem,disk=input_disk,status=input_status)

    return redirect("/manager/")



def manager(request):
    host_info_list = models.hostinfo.objects.all()
    return render(request, "manager.html",{"host_info_list": host_info_list})


def save_data(request):
    if request.method == "POST":
        ret = {"status": True, "error": ""}
        try:
            RecData = json.loads(request.POST["data"])
            print(RecData)
            for i in RecData:
                dataId = int(i["id"])
                models.hostinfo.objects.filter(id=dataId).update(hostname=i["hostname"], ip=i["ip"], port=i["port"], cpu=i["cpu"], mem=i["mem"], disk=i["disk"], status=i["status"])

        except Exception as e:
            print(e)
            ret["status"] = False
            ret["error"] = str(e)

        # return HttpResponse("ok")
        return HttpResponse(json.dumps(ret))


def delete_data(request):
    if request.method == "POST":
        ret = {"status": True, "error": ""}
        try:
            dataId = json.loads(request.POST["data"])
            for i in dataId:
                print(i)
                models.hostinfo.objects.filter(id=int(i)).delete()

        except Exception as e:
            ret["status"] = False
            ret["error"] = str(e)
        return HttpResponse(json.dumps(ret))

def test(request):
    print(test)
    return render(request,"child.html")
