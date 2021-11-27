from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse


# Create your views here.

def index(request):
    # usuarios = User.objects.all()
    response = requests.get('http://127.0.0.1:8000/user/')
    todos = response.json()
    return render(request, "app/index.html", {"users": todos})


def delete(request, id):
    x = requests.delete('http://127.0.0.1:8000/user/' + id)

    return redirect("/app/")


def actualizar(request, id):
    # usuarios = User.objects.all()
    response = requests.get('http://127.0.0.1:8000/user/' + id)
    user = response.json()
    return render(request, "app/update.html", {"user": user})


def create(request):
    url = 'http://127.0.0.1:8000/user/'

    username = request.POST.get('name', 'none')
    userLastname = request.POST.get('lastname', 'none')
    userIdType = request.POST.get('idtype', 'none')
    userIdNum = request.POST.get('idnum', 'none')
    userCity = request.POST.get('city', 'none')
    myUser = {'idType': userIdType,
              'idNum': userIdNum,
              'name': username,
              'lastName': userLastname,
              'city': userCity
              }

    x = requests.post(url, data=myUser)

    return redirect("/app/index/")


def update(request):
    userId = request.POST.get('userId', 'userId')
    url = 'http://127.0.0.1:8000/user/' + userId

    username = request.POST.get('name', 'none')
    userLastname = request.POST.get('lastname', 'none')
    userIdType = request.POST.get('idtype', 'none')
    userIdNum = request.POST.get('idnum', 'none')
    userCity = request.POST.get('city', 'none')
    myUser = {'idType': userIdType,
              'idNum': userIdNum,
              'name': username,
              'lastName': userLastname,
              'city': userCity
              }

    x = requests.put(url, data=myUser)

    return redirect("/app/index/")
