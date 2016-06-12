from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def note(request):
    return render(request, 'note.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        return render(request, 'register.html')
    else:
        return render(request, 'login.html')

