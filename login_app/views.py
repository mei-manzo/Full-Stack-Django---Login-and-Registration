from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "index.html")

def check_registration(request):
    errors = User.objects.basic_validator(request.POST)
    email = request.POST['email']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #changed to check len of dictionary
    elif len(User.objects.filter(email=email)) >= 1:
        messages.error(request, "Email is already in use")
        return redirect('/')
    else:
        new_user = User.objects.create(first_name = request.POST['first-name'], last_name = request.POST['last-name'], email = request.POST['email'], password = request.POST['password'])
        return redirect('/success')

def check_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        return redirect('/success')


def success(request):
    context = {
        "current_user" : User.objects.last()
    }
    return render(request, "success.html", context)

# def logout(request):
#     request.session.flush()
#     return redirect('/')