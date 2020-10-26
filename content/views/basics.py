from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def browse(request):
    return render(request, "browse.html")


def add(request):
    return render(request, "add.html")
