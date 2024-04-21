from django.shortcuts import render



def login(request):
    return render(request, "login.html",context={"nom":"admin"})


def index(request):
    return render(request, "index.html",context={"nom":"index", "page":"deux"})