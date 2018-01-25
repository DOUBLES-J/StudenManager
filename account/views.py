from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return render(request, 'account/sign_in.html')

def register(request):
    return render(request, 'account/register.html')

def checkname(request):
    return HttpResponse('ok')