from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def About(request):
    return render(request, 'main/about-us.html')


def login(request):
    return render(request, 'main/login.html')

def Serch(request):
    return render(request, 'main/serch.html')

def account(request):
    return render(request, 'main/account.html')

def Reg(request):
    return render(request, 'main/Reg.html')


