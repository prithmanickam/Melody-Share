from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import SongForm
from .models import Song

def home(request):
    return render(request, 'main/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'main/register.html', {'form': form})

def make_music(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'main/make_music.html', context)


def profile(request):
    songs = Song.objects.all()
    return render(request, 'main/profile.html', {
        'songs': songs
    })

def view_music(request):
    songs = Song.objects.all()
    return render(request, 'main/view_music.html', {
        'songs': songs
    })



def upload_music(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = SongForm()
    return render(request, 'main/upload_music.html', {
        'form': form
    })


def delete_music(request, pk):
    if request.method == 'POST':
        song = Song.objects.get(pk=pk)
        song.delete()
    return redirect('profile')


def like_music(request, pk):
    if request.method == 'POST':
        song = Song.objects.get(pk=pk)
        song.like()
        song.save()
    return redirect('view_music')

#@login_required()

