from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import Person

# Create your views here.
def home(request):
    if request.method == 'GET':
        email=request.GET.get("emailadres")
        password=request.GET.get("pass")
        try:
            person=Person.objects.get(email=email)
            request.session["email"]=email
            return HttpResponseRedirect('/home/')
        except:
            return render(request,"giris.html", {})

    # if a GET (or any other method) we'll create a blank form

    return render(request,"giris.html", {})
