from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html') 
def about(request):
    return render(request, 'main/about.html')
def notes(request):
    return render(request, 'main/notes.html')
def music(request):
    return render(request, 'main/music.html')
def chat(request):
    return render(request, 'main/chat.html')