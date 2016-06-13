from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags', 'username']

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/note/')
    else:
        return HttpResponseRedirect('/login/')

def note(request, pk = 1):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    note_list = Note.objects.all().filter(username=request.user.username)
    this_note = Note.objects.get(pk = pk)
    tag_list = this_note.tags.split(',')
    return render(request, 'note.html', {
            'username': request.user.username,
            'note_list': note_list,
            'this_note': this_note,
            'tag_list': tag_list,
        })

def note_create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            this_note = form.save()
            return HttpResponseRedirect('/note/'+str(this_note.pk))

    return render(request, 'note_create.html', {
            'username': request.user.username,
        })

def note_edit(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    this_note = Note.objects.get(pk = pk)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            this_note.title = request.POST['title']
            this_note.tags = request.POST['tags']
            this_note.content = request.POST['content']
            this_note.save()
            return HttpResponseRedirect('/note/'+str(this_note.pk))

    this_note = Note.objects.get(pk = pk)
    return render(request, 'note_edit.html', {
            'this_note': this_note,
        })

def note_delete(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    Note.objects.get(pk = pk).delete()
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username = username, password = password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html', {})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def analyze(request, tag):
    result_list = []
    for note in Note.objects.all():
        if note.tags.find(tag)!=-1:
            result_list.append(note)

    return render(request, 'tag.html', locals())
