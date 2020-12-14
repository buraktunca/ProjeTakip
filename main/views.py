from django.shortcuts import render
from .models import Project,Person,autority,indic
from django.http import HttpResponseRedirect
from random import randint
# Create your views here.

def mainpage(request):
    if "email" in request.session:
        person=Person.objects.get(email=request.session["email"])
        yetki=autority.objects.all()
        projects=Project.objects.all()
        content={"projects":projects,"person":person,"yetki":yetki}
        return render(request,"dashboard.html",content)

    else:
        return HttpResponseRedirect('/giris/')


def projectdetail(request,project_slug):
    if "email" in request.session:
        person=Person.objects.get(email=request.session["email"])
        yetki=autority.objects.all()
        projects=Project.objects.all()
        say1 = randint(600, 1500)
        say2 = randint(600, 1500)
        say3 = randint(600, 1500)
        proje=Project.objects.get(slug=project_slug)
        indikator=indic.objects.filter(proje=proje)

        content={"projects":projects,"person":person,"yetki":yetki,"proje":proje,"say1":say1,"say2":say2,"say3":say3,"indikator":indikator}
        return render(request,"proje.html",content)

    else:
            return HttpResponseRedirect('/giris/')
