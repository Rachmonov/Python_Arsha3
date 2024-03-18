from django.shortcuts import render
from myfolder.models import *
# Create your views here.

def index(malumot):

    if 'subscribe_id' in malumot.POST:
        name = malumot.POST.get('name')
        email = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        message = malumot.POST.get('message')
        idd = malumot.POST.get('subscribe_id')
        Contact(id=idd, name=name,gmail=email,subject=subject,message=message).save()
    elif malumot.method=='POST':
        email = malumot.POST.get('email')
        Subscribe(gmail=email).save()
    mening_ishim = Portfolio.objects.all()
    bizning_ishlar = Team.objects.all()
    uning_ishi = Services.objects.all()
    return render(malumot,'index.html',{'portfolios':mening_ishim,'teams':bizning_ishlar,'services':uning_ishi})

def index_port(malumot):
    return render(malumot,'portfolio-details.html')


def index_team(malumot):
    mening_ishim2 = Position.objects.all()
    return render(malumot,'index.html',{'positions':mening_ishim2})