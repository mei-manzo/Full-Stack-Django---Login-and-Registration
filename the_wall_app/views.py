from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from pytz import timezone
from login_app import views
import pytz

# def wall_success(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     # this_user = User.objects.filter(id = request.session['user_id'])
#     context = {
#         'all_messages': Message.objects.all()
#     }
#     return render(request, "success.html", context)

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "current_user" : this_user[0], #grabs from session rather than database to prevent refreshing into login
        "all_messages": Message.objects.all(),
        "newest_first": Message.objects.all().order_by("-updated_at")
    }
    return render(request, "wall.html", context)

def create_message(request):
    Message.objects.create(poster=User.objects.get(id=request.session['user_id']), message=request.POST['content'])
    return redirect('/wall')

