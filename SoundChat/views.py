from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def chat_view(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'SoundChat/chat.html', {'messages': messages})