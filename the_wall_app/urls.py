from django.urls import path     
from . import views
urlpatterns = [
    path('wall', views.wall),
    path('create_message', views.create_message),
]