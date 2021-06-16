from django.urls import path     
from . import views
urlpatterns = [
    path('wall', views.wall),
    path('create_message', views.create_message),
    path('comment/<int:id>', views.comment),
    path('profile/<int:id>', views.profile),
    path('like/<int:id>', views.like),

]