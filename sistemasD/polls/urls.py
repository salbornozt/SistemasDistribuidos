from django.urls import path
from .views import index, delete, create, update, actualizar

urlpatterns = [
    path('index/', index),
    path('delete/<id>/', delete, name="delete"),
    path('update/', update, name="update"),
    path('actualizar/<id>/', actualizar, name="actualizar"),

    path('create/', create, name="create"),

]
