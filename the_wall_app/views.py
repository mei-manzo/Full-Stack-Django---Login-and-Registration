from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "current_user" : this_user[0] #grabs from session rather than database to prevent refreshing into login
    }
    return render(request, "wall.html", context)

def create_message(request):
    # this_user = User.objects.filter(id = request.session['user_id'])
    # context = {
    #     "current_user" : this_user[0] #grabs from session rather than database to prevent refreshing into login
    # }
