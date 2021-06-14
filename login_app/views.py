from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def success(request):
    return render(request, "success.html")
