from django.urls import path
from .views import user_list, user_detail, index

urlpatterns = [
    path('user/', user_list),
    path('user/<int:pk>', user_detail),
    path('app/', index),
]
