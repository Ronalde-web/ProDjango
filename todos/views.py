from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, "todos/home.html")

def login(request):
    return render(request, "todos/login.html")


def ronalde(request):
    return render(request, "todos/ronalde.html")


