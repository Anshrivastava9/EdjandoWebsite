from django.shortcuts import render
from .models import Data,Company,Message

def index(request):
    return render(request,'index.html')

def imprenditore(request):
    return render(request,"imprenditore.html")

def sip(request):
    return render(request,"sip.html")

def blog(request):
    return render(request,"blog.html")

def messagesend(request):
    if request.method=='POST':
        msg=Message()
        msg.name=request.POST['name']
        msg.email=request.POST['email']
        msg.subject=request.POST['subject']
        msg.messaging1=request.POST['messaging1']
        msg.save()
    return render(request,"index.html")



def registercompany(request):
    if request.method=='POST':
        data1=Company()
        data1.companyname=request.POST['companyname']
        data1.email=request.POST['email']
        data1.name=request.POST['name']
        data1.address=request.POST['address']
        data1.designation=request.POST['designation']
        data1.mobilenumber=request.POST['mobilenumber']
        data1.department=request.POST['department']

        data1.save()
        return render(request,"sip.html")

    else:
        return render(request,"registercompany.html")

    

def registerstudent(request):
    if request.method=='POST':
        data=Data()
        data.name=request.POST['name']
        data.college=request.POST['college']
        data.email=request.POST['email']
        data.year=request.POST['year']
        data.branch=request.POST['branch']
        data.mobilenumber=request.POST['mobilenumber']
        data.department=request.POST['department']

        data.save()
        return render(request,"sip.html")

    else:
        return render(request,"registerstudent.html")
