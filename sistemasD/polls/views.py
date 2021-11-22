from django.shortcuts import render, redirect
import requests


# Create your views here.

def index(request):
    # usuarios = User.objects.all()
    response = requests.get('http://127.0.0.1:8000/user/')
    todos = response.json()
    return render(request, "app/index.html", {"users": todos})


def delete(request, id):
    x = requests.delete('http://127.0.0.1:8000/user/'+id)

    return redirect("/app/")


def create(request):
    #x = requests.delete('http://127.0.0.1:8000/user/'+id)

    return redirect("/app/")
