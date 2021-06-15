from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from pytz import timezone
import pytz


def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "current_user" : this_user[0] #grabs from session rather than database to prevent refreshing into login
    }
    return render(request, "wall.html", context)

def create_message(request):
    if request.method == 'POST':
        #creating date
        # date_format='%m/%d/%Y %H:%M:%S %Z'
        # date = datetime.now(tz=pytz.utc)
        # date = date.astimezone(timezone('US/Pacific'))
        # myTime = date.strftime(date_format)
        this_user = User.objects.get(id = request.session['user_id'])
        new_message = Message.objects.create(user=this_user, message=request.POST['content'])
        context = {
            "all_messages": Message.objects.all(),
            # "all_messages": Message.objects.all()
        }
        return render(request, "wall.html", context)
    return redirect("/wall")