from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def About_Us(request):
    return render(request, 'About us.html')

def error(request):
    return render(request, '404.html')

def game_list(request):
    return render(request, 'game-list.html')