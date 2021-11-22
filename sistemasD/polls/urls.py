from django.urls import path
from .views import index, delete, create

urlpatterns = [
    path('', index),
    path('delete/<id>/', delete, name="delete"),
    path('create/', create, name="create"),

]
