from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.

def hello_world (request):
    # render(request, template_name, dictionary)
    return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })

def home (request):
    postList = Post.objects.all()
    return render(request, 'home.html', {
        'postList': postList,
    })

